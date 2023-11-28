// Leetcode 53 - Maximum Subarray
// Nov. 27, 2023

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max_arr = nums[0], max_sum = 0;
    for (let i of nums) {
        max_sum = max_sum > 0 ? max_sum + i : i;
        max_arr = max_sum > max_arr ? max_sum : max_arr;
    }
    return max_arr;
};