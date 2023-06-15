import timeit
from typing import List
import numpy as np

# Leetcode 2529 (06/15/2023)
# Defining functions

# brute force
def maximumCount1(nums: List[int]):
    pos = neg = 0
    for n in nums:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
    return max(neg, pos)

# using numpy vectors
def maximumCount2(nums: List[int]):
    n = np.array(nums)
    neg = len(n[n < 0])
    pos = len(n[n > 0])
    return max(neg, pos)

def maximumCount3(nums: List[int]):
    neg = sum(1 for i in nums if i < 0)
    pos = sum(1 for i in nums if i > 0)
    return(neg, pos)

time1a = timeit.timeit(lambda: maximumCount1([-2,-1,-1,1,2,3]), number=10000)
time2a = timeit.timeit(lambda: maximumCount1([-3,-2,-1,0,0,1,2]), number=10000)
time3a = timeit.timeit(lambda: maximumCount1([5,20,66,1314]), number=10000)

time1b = timeit.timeit(lambda: maximumCount2([-2,-1,-1,1,2,3]), number=10000)
time2b = timeit.timeit(lambda: maximumCount2([-3,-2,-1,0,0,1,2]), number=10000)
time3b = timeit.timeit(lambda: maximumCount2([5,20,66,1314]), number=10000)

time1c = timeit.timeit(lambda: maximumCount3([-2,-1,-1,1,2,3]), number=10000)
time2c = timeit.timeit(lambda: maximumCount3([-3,-2,-1,0,0,1,2]), number=10000)
time3c = timeit.timeit(lambda: maximumCount3([5,20,66,1314]), number=10000)

# Print the runtimes
print("Runtime (maximumCount1):", time1a, time2a, time3a) # 1
print("Runtime (maximumCount2):", time1b, time2b, time3b) # 2
print("Runtime (maximumCount3):", time1c, time2c, time3c) # 3