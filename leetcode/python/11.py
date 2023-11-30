## Leetcode 11 - Container with Most Water
## Nov. 29, 2023

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans