## Leetcode 217 - Contains Duplicate
## Nov. 25, 2023

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for i in nums:
            if i in visited:
                return True
            visited.add(i)
        return False