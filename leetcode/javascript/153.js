// Leetcode 153 - Find Minimum in Rotated Sorted Array
// Nov. 28, 2023

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let l = 0, r = nums.length - 1;
    while (l < r) {
        let m = Math.trunc((l+r)/2);
        if (nums[r] < nums[m]) l = m + 1;
        else r = m;
    }
    return nums[r];
};