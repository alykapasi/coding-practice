// Leetcode 1 - Two Sum
// Nov. 24, 2023

/*
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let visited = {};
    for (let i in nums) {
        let c = target - nums[i];
        if (c in visited) {
            return [i, visited[c]];
        } else {
            visited[nums[i]] = i;
        }
    }
};

let i = twoSum([2,7,11,15], 9);
console.log(i);