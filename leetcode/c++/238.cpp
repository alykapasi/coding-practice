// Leetcode 238 - Product of Array Except Self
// Nov. 26, 2023

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int lhs = 1, rhs = 1, n = nums.size();
        vector<int> ans(n, 1);

        for (int i = 0; i < n; i++) {
            if (i > 0) {
                lhs *= nums[i - 1];
                ans[i] *= lhs;
            }

            if (i < n - 1) {
                rhs *= nums[n - i - 1];
                ans[n - i - 2] *= rhs;
            }
        }

        return ans;
    }
};