// Leetcode 338 - Counting Bits
// Dec. 1, 2023

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    let ans = Array(n+1).fill(0);

    for (let i = 1; i < n + 1; i++) ans[i] = ans[parseInt(i / 2)] + (i % 2);

    return ans;
};