#include "l3sap.h"
#include "l2sap.h"
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <stdio.h>

L3SAP* l3sap_create(struct L2SAP* l2) {
    if (!l2) return NULL;

    L3SAP* l3 = malloc(sizeof(L3SAP));
    if (!l3) return NULL;

    l3->l2 = l2;
    return l3;
}

void l3sap_destroy(L3SAP* l3) {
    if (l3) {
        l2sap_destroy(l3->l2);
        free(l3);
    }
}

int l3sap_sendto(L3SAP* l3, const uint8_t* data, int len) {
    return l2sap_sendto(l3->l2, data, len);
}

int l3sap_recvfrom(L3SAP* l3, uint8_t* buffer, int buffer_size) {
    return l2sap_recvfrom(l3->l2, buffer, buffer_size);
}

int l3sap_recvfrom_timeout(L3SAP* l3, uint8_t* buffer, int buffer_size, struct timeval* timeout) {
    return l2sap_recvfrom_timeout(l3->l2, buffer, buffer_size, timeout);
}
