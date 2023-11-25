## Leetcode 1 - Two Sum
## Nov. 24, 2023

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## one pass hashmap
        visited = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in visited:
                return [i, visited[c]]
            else:
                visited[nums[i]] = i
