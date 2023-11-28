## Leetcode 53 - Maximum Subarray
## Nov. 27, 2023

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_arr, max_sum = nums[0], 0
        for i in nums:
            max_sum = max(0, max_sum) + i
            max_arr = max(max_arr, max_sum)
        return max_arr
