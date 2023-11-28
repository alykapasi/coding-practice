// Leetcode 238 - Product of Array Except Self
// Nov. 26, 2023

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* ans = (int *)malloc(sizeof(int) * numsSize);
    int lhs = 1, rhs = 1;

    for (int i = 0; i < numsSize; i++) {
        ans[i] = lhs;
        lhs *= nums[i];
    }

    for (int i = numsSize - 1; i >= 0; i--) {
        ans[i] *= rhs;
        rhs *= nums[i];
    }

    return ans;
}