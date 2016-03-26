#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <assert.h>

char buffer[32];
char chunk1[32];
char chunk2[32];
char chunk4[32];

char get_bit(char c, int i) {
    return (c >> i) & 0x01;
}

int main() {
    int original_file = open("endian.txt", O_RDONLY);
    read(original_file, buffer, sizeof(char) * 32);
    printf("%s\n", buffer);

    int i;
    for (i = 0; i < 32; i++) {
        // Alright... I tried chunks of 4.. I tried chunks of 2... let's try...
        // literally reversing every fucking bit...

        char tmp = 0;

        tmp = tmp | (get_bit(buffer[i], 7) << 3);
        tmp = tmp | (get_bit(buffer[i], 6) << 2);
        tmp = tmp | (get_bit(buffer[i], 5) << 1);
        tmp = tmp | (get_bit(buffer[i], 4) << 0);
        tmp = tmp | (get_bit(buffer[i], 3) << 7);
        tmp = tmp | (get_bit(buffer[i], 2) << 6);
        tmp = tmp | (get_bit(buffer[i], 1) << 5);
        tmp = tmp | (get_bit(buffer[i], 0) << 4);
        chunk4[i] = tmp;

        tmp = 0;
        tmp = tmp | (get_bit(buffer[i], 7) << 5);
        tmp = tmp | (get_bit(buffer[i], 6) << 4);
        tmp = tmp | (get_bit(buffer[i], 5) << 7);
        tmp = tmp | (get_bit(buffer[i], 4) << 6);
        tmp = tmp | (get_bit(buffer[i], 3) << 1);
        tmp = tmp | (get_bit(buffer[i], 2) << 0);
        tmp = tmp | (get_bit(buffer[i], 1) << 3);
        tmp = tmp | (get_bit(buffer[i], 0) << 2);
        chunk2[i] = tmp;

        tmp = 0;
        tmp = tmp | (get_bit(buffer[i], 7) << 6);
        tmp = tmp | (get_bit(buffer[i], 6) << 7);
        tmp = tmp | (get_bit(buffer[i], 5) << 4);
        tmp = tmp | (get_bit(buffer[i], 4) << 5);
        tmp = tmp | (get_bit(buffer[i], 3) << 2);
        tmp = tmp | (get_bit(buffer[i], 2) << 3);
        tmp = tmp | (get_bit(buffer[i], 1) << 0);
        tmp = tmp | (get_bit(buffer[i], 0) << 1);
        chunk1[i] = tmp;

        chunk1[i] = chunk1[i] ^ chunk2[i] ^ chunk4[i];
    }

    char wtf[24] = {
        '\xbe', '\x76', '\x2c', '\x8c', '\x26', '\x76', '\xcc', '\xfa', '\xa6', '\x36',
        '\x2e', '\x2e', '\x96', '\x36', '\xfa', '\x26', '\x76', '\x2c', '\xfa', '\xe2',
        '\x92', '\x42', '\xde', '\0'
    };
    printf("%s\n\n", chunk1);
    printf("%s\n\n", chunk2);
    printf("%s\n\n", chunk4);
    printf("%s\n\n", wtf);
    close(original_file);
    return 0;
}

