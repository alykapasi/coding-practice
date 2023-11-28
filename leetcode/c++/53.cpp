// Leetcode 53 - Maximum Subarray
// Nov. 27, 2023

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_arr = nums.at(0), max_sum = 0;
        for (int i : nums) {
            max_sum = max(0, max_sum) + i;
            max_arr = max(max_arr, max_sum);
        }

        return max_arr;
    }
};