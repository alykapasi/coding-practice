// Leetcode 153 - Find Minimum in Rotated Sorted Array
// Nov. 28, 2023

#include <vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int>&nums) {
        int l = 0, r = nums.size() - 1, m;
        while (l < r) {
            m = (l+r)/2;
            if (nums[r] < nums[m]) l = m + 1;
            else r = m;
        }
        return nums[r];
    }
};