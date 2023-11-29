// Leetcode 152 - Maximum Product Subarray
// Nov. 28, 2023

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let maxVal = minVal = ans = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < 0) {
            let temp = maxVal;
            maxVal = minVal;
            minVal = temp;
        }

        maxVal = nums[i] > nums[i]*maxVal ? nums[i] : nums[i]*maxVal;
        minVal = nums[i] < nums[i]*minVal ? nums[i] : nums[i]*minVal;
        ans = ans > maxVal ? ans : maxVal;
    }
    return ans;
};