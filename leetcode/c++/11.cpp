// Leetcode 11 - Container with Most Water
// Nov. 29, 2023

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = 0 , l = 0, r = height.size() - 1;
        while (l < r) {
            int area = min(height[l], height[r]) * (r - l);
            ans = max(ans, area);
            if (height[l] < height[r]) l++;
            else r--;
        }
        return ans;
    }
};