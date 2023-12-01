// Leetcode 268 - Missing Number
// Dec. 1, 2023

int missingNumber(int* nums, int numsSize) {
    int sum_current = 0;
    for (int i = 0; i < numsSize; i++) sum_current += nums[i];
    return (numsSize*(numsSize + 1))/2 - sum_current;
}