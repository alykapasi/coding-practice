// Leetcode 15 - 3Sum
// Nov. 29, 2023

/**
 * @param {number[]} sortedNums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let sortedNums = nums.sort((a,b) => { return a - b; });
    let ans = [];
    for (let i = 0; i < sortedNums.length - 2; i++) {
        if (i > 0 && sortedNums[i] == sortedNums[i-1]) continue;
        let l = i + 1, r = sortedNums.length - 1;
        while (l < r) {
            let total = sortedNums[i] + sortedNums[l] + sortedNums[r];
            if (total === 0) {
                ans.push([sortedNums[i], sortedNums[l], sortedNums[r]]);
                while (l < r && sortedNums[l] === sortedNums[l+1]) l++;
                while (l < r && sortedNums[r] === sortedNums[r-1]) r--;
                l++;
                r--;
            } 
            else if (total < 0) l++;
            else r--;
        }
    }

    return ans;
};