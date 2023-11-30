// Leetcode 11 - Container with Most Water
// Nov. 29, 2023

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let ans = l = 0, r = height.length - 1;
    while (l < r) {
        let area = Math.min(height[l], height[r]) * (r - l);
        ans = Math.max(ans, area)
        if (height[l] < height[r]) l++;
        else r--;
    }

    return ans;
};