// Leetcode 1 - Two Sum
// Nov. 24, 2023

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> visited;
        for (int i = 0; i < nums.size(); i++) {
            int c = target - nums[i];
            if (visited.find(c) == visited.end()) {
                visited[nums[i]] = i;
            } else {
                return {visited[c], i};
            }
        }
        return {-1,-1};
    }
};