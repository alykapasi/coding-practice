## Leetcode 15 - 3Sum
## Nov. 29, 2023

from typing import List

class Solution:
    def threeSum(self, sorted_nums: List[int]) -> List[List[int]]:
        ans = []
        sorted_nums = sorted(sorted_nums)
        for i in range(0, len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            l, r = i + 1, len(sorted_nums) - 1
            while l < r:
                total = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if total == 0:
                    ans.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    while l < r and sorted_nums[l] == sorted_nums[l+1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans