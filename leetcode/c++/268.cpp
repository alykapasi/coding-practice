// Leetcode 268 - Missing Number
// Dec. 1, 2023

#include <vector>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), total = 0;
        for (auto& n: nums) total += n;
        return (n*(n+1))/2 - total;
    }
};