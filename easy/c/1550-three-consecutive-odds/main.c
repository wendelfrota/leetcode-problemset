#include <stdio.h>
#include <stdbool.h>

bool threeConsecutiveOdds(int* arr, int arrSize) {
    for (int i = 0; i <= arrSize - 3; i++)
        if (arr[i] & 1)
            if (arr[i + 1] & 1)
                if (arr[i + 2] & 1)
                    return 1;

    return 0;
}


// int main(){
//     int n1[] = {2, 6, 4, 1};
//     int n2[] = {1, 2, 34, 3, 4, 5, 7, 23, 12};
//
//     int ns1 = sizeof(n1) / sizeof(n1[0]);
//     int ns2 = sizeof(n2) / sizeof(n2[0]);
//
//     printf("%i\n", threeConsecutiveOdds(n1, ns1));
//     printf("%i\n", threeConsecutiveOdds(n2, ns2));
//
//     return 0;
// }