#ifndef L3SAP_H
#define L3SAP_H

#include <stdint.h>
#include <sys/time.h>

#define L3Headersize 0 
#define L3Framesize 1024

struct L2SAP;

typedef struct L3SAP {
    struct L2SAP* l2;
} L3SAP;

L3SAP* l3sap_create(struct L2SAP* l2);
void l3sap_destroy(L3SAP* l3);

int l3sap_sendto(L3SAP* l3, const uint8_t* data, int len);
int l3sap_recvfrom(L3SAP* l3, uint8_t* buffer, int buffer_size);
int l3sap_recvfrom_timeout(L3SAP* l3, uint8_t* buffer, int buffer_size, struct timeval* timeout);

#endif