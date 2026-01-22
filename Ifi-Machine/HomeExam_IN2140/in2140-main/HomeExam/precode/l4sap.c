#include <stdint.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#include "l4sap.h"
#include "l2sap.h"


/* Create an L4 client.
 * It returns a dynamically allocated struct L4SAP that contains the 
 * data of this L4 entity (including the pointer to the L2 entity
 * used).
 */
L4SAP* l4sap_create( const char* server_ip, int server_port )
{
    if (server_ip == NULL || server_port == 0) {
        return NULL;
    }

    struct L2SAP *l2 = l2sap_create(server_ip, server_port);
    if (l2 == NULL) {
        return NULL;
    }
    
    struct L4SAP *l4 = malloc(sizeof(struct L4SAP));
    if (l4 == NULL) {
        l2sap_destroy(l2);
        return NULL;
    }
    

    l4->l2 = l2;
    l4->seqno = 0;
    l4->ackno = 0;
    l4->reset_sent = 0;
    return l4;
}

/* The functions sends a packet to the network. The packet's payload
 * is copied from the buffer that it is passed as an argument from
 * the caller at L5.
 * If the length of that buffer, which is indicated by len, is larger
 * than L4Payloadsize, the function truncates the message to L4Payloadsize.
 *
 * The function does not return until the correct ACK from the peer entity
 * has been received.
 * When a suitable ACK arrives, the function returns the number of bytes
 * that were accepted for sending (the potentially truncated packet length).
 *
 * Waiting for a correct ACK may fail after a timeout of 1 second
 * (timeval.tv_sec = 1, timeval.tv_usec = 0). The function retransmits
 * the packet in that case.
 * The function attempts up to 4 retransmissions. If the last retransmission
 * fails with a timeout as well, the function returns L4_SEND_FAILED.
 *
 * The function may also return:
 * - L4_QUIT if the peer entity has sent an L4_RESET packet.
 * - another value < 0 if an error occurred.
 */

L4Header *get_l4header(uint8_t *pkt) {
    L4Header *header = malloc(sizeof(L4Header));
    memcpy(header, pkt, sizeof(L4Header));

    return header;
}
int l4sap_send(L4SAP* l4, const uint8_t* data, int len) {
    if (l4 == NULL || data == NULL) {
        return -1;
    }

    // L4Payloadsize = (L4Framesize-L4Headersize)
    int send_length = (len > L4Payloadsize) ? L4Payloadsize : len;

    L4Header header = {
        .type = L4_DATA,
        .seqno = l4->seqno,
        .ackno = 0,
        .mbz = 0
    };

    uint8_t packet[send_length + L4Headersize];
    memcpy(packet, &header, sizeof(L4Header));
    memcpy(packet + sizeof(L4Header), data, send_length);

    struct timeval timeout = { .tv_sec = 1, .tv_usec = 0 };
    uint8_t response[L4Framesize];

    for (int i = 0; i < 4; i++) {
        int res = l2sap_sendto(l4->l2, packet, sizeof(L4Header) + send_length);
        if (res < 0) return -2;
    
        int recv_len = l2sap_recvfrom_timeout(l4->l2, response, sizeof(response), &timeout);
        if (recv_len < 0) continue;
    
        if (recv_len >= sizeof(L4Header)) {
            L4Header* resp_header = get_l4header(response);
            //L4Header *resp_header = (L4Header *)response;
            if (resp_header->type == L4_RESET) {
                free(resp_header);
                return L4_QUIT;
            }
    
            if (resp_header->type == L4_ACK &&
                resp_header->ackno == l4->seqno) {
                l4->seqno = (l4->seqno + 1) % 256;
                free(resp_header);
                return send_length; 
            }
            

            if (resp_header->type == L4_DATA) {
                L4Header ack = {
                    .type = L4_ACK,
                    .seqno = resp_header->seqno,
                    .ackno = resp_header->seqno,
                    .mbz = 0
                };
                l2sap_sendto(l4->l2, (uint8_t*)&ack, sizeof(L4Header));
            }
            free(resp_header);
        }
    }
    
    return L4_SEND_FAILED;
}
/* The functions receives a packet from the network. The packet's
 * payload is copy into the buffer that it is passed as an argument
 * from the caller at L5.
 * The function blocks endlessly, meaning that experiencing a timeout
 * does not terminate this function.
 * The function returns the number of bytes copied into the buffer
 * (only the payload of the L4 packet).
 * The function may also return:
 * - L4_QUIT if the peer entity has sent an L4_RESET packet.
 * - another value < 0 if an error occurred.
 */
int l4sap_recv(L4SAP* l4, uint8_t* data, int len) {
    if (l4 == NULL || data == NULL || len <= 0) {
        return -1;
    }

    uint8_t buffer[L4Framesize];
    int received = l2sap_recvfrom(l4->l2, buffer, L4Framesize);

    L4Header* l4_header = get_l4header(buffer);

    if (l4_header->type == L4_RESET) {
        free(l4_header);
        return L4_QUIT;
    }

    if (l4_header->type == L4_DATA) {
        int payload_len = received - sizeof(L4Header);
        if (payload_len > len) payload_len = len;

        memcpy(data, buffer + sizeof(L4Header), payload_len);

        L4Header ack_header = {
            .type = L4_ACK,
            .seqno = l4_header->seqno,
            .ackno = (l4_header->seqno + 1) % 256,
            .mbz = 0
        };

        l2sap_sendto(l4->l2, (uint8_t*)&ack_header, sizeof(L4Header));

        free(l4_header);
        return payload_len;
    }

    free(l4_header);
    return -1;
}
/** This function is called to terminate the L4 entity and
 *  free all of its resources.
 *  We recommend that you send several L4_RESET packets from
 *  this function to ensure that the peer entity is also
 *  terminating correctly.
 */
void l4sap_destroy( L4SAP* l4 )
{
    if (l4 == NULL) {
        return;
    }

   uint8_t buffer[L4Framesize];
   memset(buffer, 0, L4Framesize);

   //Type
   buffer[0] = L4_RESET;
   //seqno
   buffer[1] = l4->seqno;
   //ackno
   buffer[2] = l4->ackno;

    for (int i = 0; i < 3; i++) {
        //3 bytes for type, seqno and ackno
        l2sap_sendto(l4->l2, buffer, 3);
        //100ms delay
        usleep(100000);
    }

    if (l4->l2 != NULL) {
        l2sap_destroy(l4->l2);
    }

    free(l4);
}

