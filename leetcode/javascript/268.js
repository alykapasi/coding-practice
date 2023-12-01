// Leetcode 268 - Missing Number
// Dec. 1, 2023

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    return parseInt((nums.length * (nums.length + 1)) / 2) - nums.reduce((a,b) => {return a + b});
};