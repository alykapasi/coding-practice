## leetcode problem 896
## https://leetcode.com/problems/monotonic-array/

## september 03, 2023

from typing import List

def isMonotonic(nums: List[int]) -> bool:
    sorted_nums = sorted(nums)
    return nums == sorted_nums or nums == sorted_nums[::-1]


print(isMonotonic([1,2,2,3]))
print(isMonotonic([6,5,4,4]))
print(isMonotonic([1,3,2]))

