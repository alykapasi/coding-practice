// Leetcode 371 - Sum of Two Integers
// Nov. 29, 2023

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    let c;
    while (b) {
        c = a & b;
        a ^= b;
        b = c << 1;
    }
    return a;
};