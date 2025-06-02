#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *gcdOfStrings(char *str1, char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    char *x = malloc(sizeof(char) * (len2 + 1));
    char *merge1 = malloc(sizeof(char) * (len1 + len2 + 1));
    char *merge2 = malloc(sizeof(char) * (len1 + len2 + 1));

    strcpy(merge1, str1);
    strcat(merge1, str2);
    strcpy(merge2, str2);
    strcat(merge2, str1);

    if (strcmp(merge1, merge2) != 0) {
        free(merge1);
        free(merge2);
        strcpy(x, "");
        return x;
    }

    int gcd;
    for (int i = 1; i <= len2; i++) {
        if (len1 % i == 0 && len2 % i == 0) {
            gcd = i;
        }
    }

    for (int i = 0; i < gcd; i++) {
        x[i] = str2[i];
    }
    x[gcd] = '\0';

    free(merge1);
    free(merge2);
    return x;
}

int main() {
    char *x;
    x = gcdOfStrings("abcabc", "abc");
    printf("%s", x);
    free(x);
    return 0;
}