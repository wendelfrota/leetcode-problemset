#include <stdio.h>
#include <stdlib.h>

int scoreOfString(char* s) {
    int sum = 0;

    for(int i = 0; s[i + 1] != '\0'; i++)
        sum += abs(s[i] - s[i + 1]);

    return sum;
}

// int main() {
//     printf("%i", scoreOfString("hello"));
//
//     return 0;
// }