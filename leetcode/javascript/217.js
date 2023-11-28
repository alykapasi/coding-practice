// Leetcode 217 - Contains Duplicate
// Nov. 25, 2023

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let visited = new Set();
    for (let i of nums) {
        if (visited.has(i)) return true;
        visited.add(i);
    }
    return false;
};