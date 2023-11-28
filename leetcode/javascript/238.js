// Leetcode 238 - Product of Array Except Self
// Nov. 26, 2023

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length, lhs = 1, rhs = 1;
    let ans = new Array(n).fill(1);

    for (let i = 0; i < nums.length; i++) {
        if (i > 0) {
            lhs *= nums[i-1];
            ans[i] *= lhs;
        }

        if (i < n - 1) {
            rhs *= nums[n - i - 1];
            ans[n - i - 2] *= rhs;
        }
    }
    return ans;
};