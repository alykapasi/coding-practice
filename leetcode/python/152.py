## Leetcode 152 - Maximum Product Subarray
## Nov. 28, 2023

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val, min_val, ans = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            if i < 0:
                max_val, min_val = min_val, max_val
            max_val = max(i, i*max_val)
            min_val = min(i, i*min_val)
            ans = max(ans, max_val)
        return ans