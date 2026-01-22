/*
 * Add the include files that you need. "man" can help you find them.
 * You will probably need stdio.h for printf and fprintf
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "apple-todo.h"

/*
 * Find the requirements for these functions in the assignment text.
 */
int locateworm( char* buffer ){

    for(int i = 0; i < strlen(buffer); i++){
        if(buffer[i] == 'w'){
            return i;
        }
    }
    return -1;
}

int removeworm( char* apple ){
    int last_m = -1;    
    int start = locateworm(apple);
    if(start == -1){ 
        return -1;
    }

    for(int i = start; i < strlen(apple); i++){
        if (apple[i] == 109){
            last_m = i;
        }
    }

    for(int j = start; j < last_m + 1; j++){
        apple[j] = 32;
    }

    return last_m - start + 1; // +1 to be inclusive
}

