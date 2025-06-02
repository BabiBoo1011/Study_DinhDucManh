#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool *kidsWithCandies(int *candies, int candiesSize, int extraCandies, int *returnSize) {
    bool *result = malloc(sizeof(int) * candiesSize);
    *returnSize = candiesSize;

    for (int i = 0; i < candiesSize; i++) {
        int check = 1;
        int totalCandies = candies[i] + extraCandies;
        for (int j = 0; j < candiesSize; j++) {
            if (totalCandies < candies[j]) {
                check = 0;
                break;
            }
        }
        result[i] = check;
    }
    return result;
}

int main() {
    int candies[] = {2, 3, 5, 1, 3};
    int extraCandies = 3;
    int returnSize;

    bool *res = kidsWithCandies(candies, 5, extraCandies, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%s ", res[i] ? "true" : "false");
    }

    free(res);
    return 0;
}