## leetcode problem 1480 
## https://leetcode.com/problems/running-sum-of-1d-array/

## september 03, 2023

from typing import List

def runningSum(nums: List[int]) -> List[int]:
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))