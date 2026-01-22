#include <stdio.h>
#include <string.h>

void vowelshift(char *buffer, char repl) {
    const char *vowels = "aeiou";
    while (*buffer) {
        if (strchr(vowels, *buffer)) {
            *buffer = repl;
            }
        buffer++;
    }
}
