#include <stdio.h>
#include <stdbool.h>
//[1,0,0,0]
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    for(int i=0 ; i< flowerbedSize ; i++){
        int emptyleft = (i==0 || flowerbed[i-1] == 0);
        int emptyRight = (i == flowerbedSize - 1 || flowerbed[i + 1] == 0);
        if(flowerbed[i] == 0){
            if(emptyleft && emptyRight){
                flowerbed[i] = 1;
                n--;
                if (n == 0) return true;
            }
        }
    }
    
    return n<=0;
}

int main() {
    int flowerbed[] = {1,0,0,0};

    printf("%s", canPlaceFlowers(flowerbed, 4, 1) ? "true" : "false");

    return 0;
}