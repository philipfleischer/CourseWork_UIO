#include <netinet/in.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

#include "l2sap.h"

#define MAX_L2_FRAMESIZE 1024
#define HEADER_SIZE 8 // likely better to just use sizeof(L2Header).
#define CHECKSUM_INDEX 6

/* compute_checksum is a helper function for l2_sendto and
 * l2_recvfrom_timeout to compute the 1-byte checksum both
 * on sending and receiving and L2 frame.
 */

static uint8_t compute_checksum( const uint8_t* frame, int len ) {
    uint8_t checksum = 0;
    for (int i = 0; i < len; i++) {
        if (i == CHECKSUM_INDEX) {
            continue;
        }
        checksum ^= (uint8_t) frame[i];
    }

    return checksum;
}

void err(int val, int err_val, char *msg) {
    if (val == err_val) {
        perror(msg);
        exit(EXIT_FAILURE);
    }
}

L2SAP* l2sap_create(const char* server_ip, int server_port) {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    err(sock, -1, "socket error");

    // convert ip from str to sockaddr_in
    struct in_addr ip_addr;
    struct sockaddr_in addr;
    inet_pton(AF_INET, server_ip, &ip_addr);

    addr.sin_family = AF_INET;
    addr.sin_port = htons(server_port);
    addr.sin_addr = ip_addr;

    L2SAP *sap = malloc(sizeof(L2SAP));
    sap->socket = sock;
    // I set peer addr to its own addr.
    // This does not make sense but makes even less sense to do 
    // differently anywhere else. Also - it works :)
    sap->peer_addr = addr; 

    return sap;
}

void l2sap_destroy(L2SAP* client) {
    close(client->socket);
    free(client);
}

/* l2sap_sendto sends data over UDP, using the given UDP socket
 * sock, to a remote UDP receiver that is identified by
 * peer_address.
 * The parameter data points to payload that L3 wants to send
 * to the remote L3 entity. This payload is len bytes long.
 * l2_sendto must add an L2 header in front of this payload.
 * When the payload length and the L2Header together exceed
 * the maximum frame size L2Framesize, l2_sendto fails.
 */

 uint8_t *prepend_header(const uint8_t *data, L2Header *header, int len) {
    uint8_t *frame = malloc(sizeof(L2Header) + len);
    memcpy(frame, header, sizeof(L2Header));
    memcpy(frame + sizeof(L2Header), data, len);

    return frame;
}

void strip_header(uint8_t *frame, int len) {
    memmove(frame, frame + sizeof(L2Header), len); 
}

int l2sap_sendto( L2SAP* client, const uint8_t* data, int len ) {
    L2Header header;
    header.dst_addr = htonl(client->peer_addr.sin_addr.s_addr);
    header.len = htons(len + L2Headersize); 
    header.checksum = 0; 
    header.mbz = 0;

    if (ntohs(header.len) > L2Framesize) {
        fprintf(stderr, "Payload of size <%d> exceeds limit <%d> -> dropping frame\n", 
                len, L2Framesize - L2Headersize);
        return -1;
    }

    uint8_t *frame = prepend_header(data, &header, len);

    header.checksum = compute_checksum(frame, len + L2Headersize);
    memcpy(frame, &header, sizeof(L2Header)); // add in the new header containing a checksum

    int rc = sendto(
        client->socket,
        frame,
        len + L2Headersize,
        0,
        (struct sockaddr *)&client->peer_addr,
        sizeof(struct sockaddr_in)
    );

    err(rc, -1, "sendto error");
    free(frame);

    return rc;
}

/* Convenience function. Calls l2sap_recvfrom_timeout with NULL timeout
 * to make it waits endlessly.
 */
int l2sap_recvfrom( L2SAP* client, uint8_t* data, int len )
{
    return l2sap_recvfrom_timeout( client, data, len, NULL );
}

/* l2sap_recvfrom_timeout waits for data from a remote UDP sender, but
 * waits at most timeout seconds.
 * It is possible to pass NULL as timeout, in which case
 * the function waits forever.
 *
 * If a frame arrives in the meantime, it stores the remote
 * peer's address in peer_address and its size in peer_addr_sz.
 * After removing the header, the data of the frame is stored
 * in data, up to len bytes.
 *
 * If data is received, it returns the number of bytes.
 * If no data is reveid before the timeout, it returns L2_TIMEOUT,
 * which has the value 0.
 * It returns -1 in case of error.
 */

int l2sap_recvfrom_timeout( L2SAP* client, uint8_t* data, int len, struct timeval* timeout ) {
    if(len > L2Framesize) {
        printf("Attempting to recieve gt L2Framesize, changing len to L2Framesize");
        len = L2Framesize;
    }

    int ready, rc;
    fd_set rfd; // wrfd, exceptfd
    FD_ZERO(&rfd);
    FD_SET(client->socket, &rfd);

    // sock+1 because it checks n - 1 fds, i.e., it would check 0 fds if we don't +1.
    // We only intend to timeout reading (recieving),
    // therefore write/except fds are passed as NULL.
    ready = select(client->socket+1, &rfd, NULL, NULL, timeout);

    if (ready == -1) {
        perror("Select error");
        return -1;
    } else if (ready == 0) {
        fprintf(stderr, "Recieve operation timed out\n");
        return L2_TIMEOUT;
    }

    socklen_t addr_len = sizeof(client->peer_addr);
    uint8_t buf[L2Framesize];

    rc = recvfrom(
        client->socket,
        buf,
        len,
        0,
        (struct sockaddr *)&client->peer_addr,
        &addr_len
    );

    if (rc == -1) {
        perror("recieve error");
    }

    L2Header *header = (L2Header *)buf;
    header->len = ntohs(header->len);

    uint8_t recv_checksum = compute_checksum(buf, header->len);


    if (header->checksum != recv_checksum) {
        fprintf(stderr, "Checksum mismatch [%d] != [%d] -> dropping frame\n", header->checksum, recv_checksum);
        return -1;
    }

    strip_header(buf, header->len - L2Headersize);
    memcpy(data, buf, rc - L2Headersize);

    return rc - L2Headersize;
}
