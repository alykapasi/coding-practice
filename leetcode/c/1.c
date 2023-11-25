// Leetcode 1 - Two Sum
// Nov. 24, 2023

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int *ans = (int*)malloc(sizeof(int)*2);
    for (ans[0] = 0; ans[0] < numsSize - 1; ans[0]++) {
        for (ans[1] = ans[0] + 1; ans[1] < numsSize; ans[1]++) {
            if (nums[ans[0]] + nums[ans[1]] == target) goto end;
        }
    }
    end:
    return ans;
}