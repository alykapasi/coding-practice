// Leetcode 217 - Contains Duplicate
// Nov. 25, 2023

#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> visited;
        for (int i : nums) {
            if (visited.find(i) != visited.end()) return true;
            visited.insert(i);
        }
        return false;
    }
};