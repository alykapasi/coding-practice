// Leetcode 152 - Maximum Product Subarray
// Nov. 28, 2023

int maxProduct(int* nums, int numsSize) {
    int max_val = nums[0], min_val = nums[0], ans = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < 0){
            max_val ^= min_val;
            min_val ^= max_val;
            max_val ^= min_val;
        }

        max_val = nums[i] > nums[i]*max_val ? nums[i] : nums[i]*max_val;
        min_val = nums[i] < nums[i]*min_val ? nums[i] : nums[i]*min_val;
        ans = ans > max_val ? ans : max_val;
    }

    return ans;
}