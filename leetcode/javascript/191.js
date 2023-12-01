// Leetcode 191 - Number of 1 Bits
// Nov. 30, 2023

var hammingWeight = function(n) {
    let ans = 0;
    while (n) {
        ans += (n & 1);
        n >>>= 1;
    }
    return ans;
};
