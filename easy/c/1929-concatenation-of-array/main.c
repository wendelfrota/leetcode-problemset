#include <stdio.h>
#include <stdlib.h>

int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize * 2;
    int* ans = malloc(*returnSize * sizeof(int));

    for(int i = 0; i < numsSize; i++) {
        ans[i] = nums[i];
        ans[i + numsSize] = nums[i];
    }

    return ans;
}

//int main(){
//    int nums[] = {1, 2, 4};
//    int numsSize = sizeof(nums) / sizeof(nums[0]);
//    int returnSize = 0;
//
//    int* con = getConcatenation(nums, numsSize, &returnSize);
//
//    for (int i = 0; i < returnSize; i++)
//        printf("%d ", con[i]);
//
//    return 0;
//}