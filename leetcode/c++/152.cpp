// Leetcode 152 - Maximum Product Subarray
// Nov. 28, 2023

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_val = nums[0], min_val = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) swap(min_val, max_val);
            max_val = max(nums[i], nums[i]*max_val);
            min_val = min(nums[i], nums[i]*min_val);
            ans = max(ans, max_val);
        }
        return ans;
    }
};