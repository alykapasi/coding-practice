## Leetcode 238 - Product of Array Except Self
## Nov. 26, 2023

from typing import List
from math import prod

class Solution:
    def productExceptSelf(selfm, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        lhs, rhs = 1,1

        for i in range(n):
            if i > 0:
                lhs *= nums[i - 1]
                ans[i] *= lhs
            if i < n - 1:
                rhs *= nums[n - i - 1]
                ans[n - i - 2] *= rhs
        
        return ans