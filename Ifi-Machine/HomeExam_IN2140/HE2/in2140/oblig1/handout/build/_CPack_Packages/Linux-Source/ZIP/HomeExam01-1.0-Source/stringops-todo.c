/*
 * Add the include files that you need. "man" can help you find them.
 * You will probably need stdio.h for printf and fprintf
 */
#include <stdio.h>
#include <string.h>
#include "stringops-todo.h"

/*
 * Find the requirements for these functions in the assignment text.
 */
int stringsum( char *s ){
    int sum = 0;
    for (int i = 0; i < strlen(s); i++){
        if (s[i] == 32){
            continue;
        }
        int val = (int)s[i] - 64; //ASCII val of A is 64 
        if (val <= 0 || val > 58 || (val >= 27 && val <= 32)){ 
            // Checks if outside of alphabet chars or the symbols between upper- and lowercase letters
            return -1;
        }
        if (val > 26){ // if lowercase
            val -= 32;
        }
        sum += val;

    }
    return sum;
}

int   distance_between( char *s, char c ){
    int first_pos = -1; 
    int last_pos = -1;
    for(int i = 0; i < strlen(s); i++){
        if (s[i] == c){
            if(first_pos == -1){
                first_pos = i;
            } else {
                last_pos = i;
            }
        }
    }
    if (first_pos == -1){
        return -1;
    } else if (last_pos == -1){
        return 0;
    }
    return last_pos - first_pos;
}

char* string_between( char *s, char c ){
    int first_pos = -1; 
    int last_pos = -1;
    for(int i = 0; i < strlen(s); i++){
        if (s[i] == c){
            if(first_pos == -1){
                first_pos = i;
            } else{
                last_pos = i;
            }
        }
    }
    if (first_pos == -1){
        return NULL;
    }
    if(last_pos == -1){
        return "";
    }
    s[last_pos] = 0;
    return &s[first_pos+1];
}

int  stringsum2( char *s, int *res )
{
    *res = stringsum(s);
    if (res > 0){
        return 0;
    }
    return -1;
}


