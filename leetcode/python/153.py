## Leetcode 153 - Find Minimum in Rotated Sorted Array
## Nov. 28, 2023

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = int((l+r)/2)
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]

Solution().findMin([4,5,6,7,0,1,2])