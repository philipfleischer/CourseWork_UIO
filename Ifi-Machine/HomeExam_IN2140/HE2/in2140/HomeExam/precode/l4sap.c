#include <stdint.h>
#include <stdbool.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#include "l2sap.h"
#include "l3sap.h"
#include "l4sap.h"


/* Create an L4 client.
 * It returns a dynamically allocated struct L4SAP that contains the 
 * data of this L4 entity (including the pointer to the L2 entity
 * used).
 */
L4SAP* l4sap_create( const char* server_ip, int server_port )
{
    struct L2SAP* l2 = l2sap_create(server_ip, server_port);
    if (!l2) {
        return NULL;
    }

    struct L3SAP* l3 = l3sap_create(l2);
    if (!l3) {
        l2sap_destroy(l2);
        return NULL;
    }

    struct L4SAP* l4 = malloc(sizeof(L4SAP));
    if (!l4) {
        l3sap_destroy(l3);
        l2sap_destroy(l2);
        return NULL;
    }

    l4->l3 = l3;
    l4->seqno = 0;
    l4->ackno = 0;
    l4->reset_sent = 0;
    l4->has_buffered_data = false;

    return l4;
}

//Reading the L4Header for the packet
L4Header *get_l4header(const uint8_t *pkt) {
    L4Header *header = malloc(sizeof(L4Header));
    memcpy(header, pkt, sizeof(L4Header));


    return header;
}

/*
This function is used by both l4sap_send() and l4sap_recv()
to handle incoming packets.
It handles: 
    - ACK-messages (as answers on sent packets)
    - RESET (that terminates the connection)
    - DATA (that gets handles in receive, but also has to be ACK-ed )
*/

//Full Duplex function
int handle_incoming_packet( L4SAP* l4, const uint8_t* buffer, int received, uint8_t* out_data, int out_len ) 
{
    if (received < sizeof(L4Header)) return -1;

    L4Header* header = get_l4header(buffer);
    if (!header) return -1;

    if (header->type == L4_RESET) {
        free(header);
        return L4_QUIT;
    }

    if (header->type == L4_ACK) {
        int ackno = header->ackno;
        free(header);
        return ackno;
    }

    if (header->type == L4_DATA) {
        int payload_len = received - sizeof(L4Header);
    
        if (out_data != NULL && out_len > 0) {
            int copy_len = (payload_len < out_len) ? payload_len : out_len;
            memcpy(out_data, buffer + L4Headersize, copy_len);
    
            // Send ACK
            L4Header ack = {
                .type = L4_ACK,
                .seqno = header->seqno,
                .ackno = (header->seqno + 1) % 2,
                .mbz = 0
            };
            l3sap_sendto(l4->l3, (uint8_t*)&ack, sizeof(L4Header));
            int seq = header->seqno;
            free(header);
    
            return 256 + seq;
        }
    
        memcpy(l4->recv_buffer, buffer, received);
        l4->recv_buffer_len = received;
        l4->has_buffered_data = true;
    
        //Sending ack if the buffer is empty
        L4Header ack = {
            .type = L4_ACK,
            .seqno = header->seqno,
            .ackno = (header->seqno + 1) % 2,
            .mbz = 0
        };
        l3sap_sendto(l4->l3, (uint8_t*)&ack, sizeof(L4Header));
        int seq = header->seqno;
        free(header);
        return 256 + seq;
    }

    free(header);
    return -1;
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
/*
Send a packet and wait for correct ACK. 
Used to simultanuosly handle incoming DATA packets for FULL DUPLEKS
*/
int l4sap_send( L4SAP* l4, const uint8_t* data, int len ) 
{
    if (l4 == NULL || data == NULL) {
        return -1;
    }

    int send_length = (len > L4Payloadsize) ? L4Payloadsize : len;

    //Setting up an L4-Header for DATA
    L4Header header = {
        .type = L4_DATA,
        .seqno = l4->seqno,
        .ackno = 0,
        .mbz = 0
    };

    //Building the whole packet: header + payload
    uint8_t packet[send_length + L4Headersize];
    memcpy(packet, &header, sizeof(L4Header));
    memcpy(packet + sizeof(L4Header), data, send_length);

    struct timeval timeout = { .tv_sec = 1, .tv_usec = 0 };
    uint8_t response[L4Framesize];

    int expected_ack = (l4->seqno + 1) %2;

    for (int i = 0; i < 4; i++) {
        int res = l3sap_sendto(l4->l3, packet, sizeof(L4Header) + send_length);
        if (res < 0) return -2;

        //While we wait for ACK message, we can receive DATA packet, for FUll DUPLEKS
        while (1) {    
            int recv_len = l3sap_recvfrom_timeout(l4->l3, response, sizeof(response), &timeout);
            if (recv_len <= 0){
                break;
            } 

            int result = handle_incoming_packet(l4, response, recv_len, NULL, 0);
            if (result == L4_QUIT) {
            
                return L4_QUIT;
            }
            if (result == expected_ack) {
            
                l4->seqno = expected_ack;
                return send_length;
            } 
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

 /*
 Receive packets from the network and blocks until something gets received. 
 Also able to handle other types of packets like ACKs to guarantee FullDupleks!
 */
int l4sap_recv(L4SAP* l4, uint8_t* data, int len) 
{
    if (l4 == NULL || data == NULL || len <= 0) return -1;

    // Hvis vi allerede har buffered data fra en tidligere DATA-pakke
    if (l4->has_buffered_data) {
        int payload_len = l4->recv_buffer_len - sizeof(L4Header);
        int copy_len = (payload_len < len) ? payload_len : len;

        memcpy(data, l4->recv_buffer, copy_len);
        l4->has_buffered_data = false;
        l4->recv_buffer_len = 0;

        return copy_len;
    }

    while (1) {
        uint8_t buffer[L4Framesize];
        int received = l3sap_recvfrom(l4->l3, buffer, sizeof(buffer));
        if (received <= 0) continue;

        int result = handle_incoming_packet(l4, buffer, received, data, len);


        if (result == L4_QUIT) return L4_QUIT;

        if (result >= 256) {
            int payload_len = received - sizeof(L4Header);
            return payload_len;
        }
    }
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

   buffer[0] = L4_RESET;
   buffer[1] = l4->seqno;
   buffer[2] = l4->ackno;

    //Looping 3 times to increase chance of deleting correct packet
    for (int i = 0; i < 3; i++) {
        l3sap_sendto(l4->l3, buffer, 3);
        usleep(100000);
    }

    if (l4->l3 != NULL) {
        l3sap_destroy(l4->l3);
    }

    free(l4);
}

