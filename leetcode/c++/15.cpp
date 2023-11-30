// Leetcode 15 - 3Sum
// Nov. 29, 2023

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 2; i++) {
            if (i == 0 || nums[i] != nums[i-1]) {
                int l = i + 1, r = nums.size() - 1;
                while (l < r) {
                    int total = nums[i] + nums[l] + nums[r];
                    if (total < 0 || (l > i + 1 && nums[l] == nums[l-1])) l++;
                    else if (total > 0 || (r < nums.size() - 1 && nums[r] == nums[r+1])) r--;
                    else ans.push_back({nums[i], nums[l++], nums[r--]});
                }
            }
        }

        return ans;
    }
};
