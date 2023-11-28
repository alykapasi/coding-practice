// Leetcode 53 - Maximum Subarray
// Nov. 27, 2023

int maxSubArray(int* nums, int numsSize) {
    int max_arr = nums[0], max_sum = 0;
    for (int i = 0; i < numsSize; i++) {
        max_sum = max_sum > 0 ? max_sum + nums[i] : nums[i];
        max_arr = max_sum > max_arr ? max_sum : max_arr;
    }
    return max_arr;
}