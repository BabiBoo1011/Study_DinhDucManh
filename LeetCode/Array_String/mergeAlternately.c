#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *mergeAlternately(char *s1, char *s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);

    char *merge = malloc(sizeof(char) * (len1 + len2 + 1));
    int i = 0, j = 0, k = 0;

    if (len1 == len2) {
        while (i < len1) {
            merge[k] = s1[i];
            k++;
            merge[k] = s2[j];
            k++;
            i++;
            j++;
        }
    } else if (len1 > len2) {
        while (i < len2) {
            merge[k] = s1[i];
            k++;
            merge[k] = s2[j];
            k++;
            i++;
            j++; 
        }
        while (i < len1) {
            merge[k] = s1[i];
            k++;
            i++;
        }
    } else {
        while (i < len1) {
            merge[k] = s1[i];
            k++;
            merge[k] = s2[j];
            k++;
            i++;
            j++;
        }
        while (j < len2) {
            merge[k] = s2[j];
            k++;
            j++;
        }
    }
    merge[k] = '\0';

    return merge;
}

int main() {
    char *merge;

    merge = mergeAlternately("ab", "def");

    printf("%s", merge);

    free(merge);

    return 0;
}