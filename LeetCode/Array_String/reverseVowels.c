#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverseVowels(char* s) {
    char *vowels = malloc(strlen(s) + 1);
    int sizeS = strlen(s);

    int j = 0;
    for (int i = 0; i < sizeS; i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'u' ||s[i] == 'o' ||
            s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'U' || s[i] == 'O') {
            vowels[j] = s[i];
            j++;    
        }
    }
    vowels[j] = '\0';

    for (int i = 0; i < strlen(vowels) / 2; i++) {
        char tmp = vowels[i];
        vowels[i] = vowels[j - 1 - i];
        vowels[j - 1 - i] = tmp;
    }

    int k = 0;
    for (int i = 0; i < sizeS; i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'u' || s[i] == 'o' ||
            s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'U' || s[i] == 'O') {
            s[i] = vowels[k];
            k++;
        }
    }
    return s;
}