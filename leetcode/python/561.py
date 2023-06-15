import timeit
from typing import List
from itertools import permutations

# Leetcode 561 (06/14/2023)
# Defining functions

# Brute force solution
def arraySumPair1(nums: List[int]):
    combos = list(permutations(nums, len(nums)))
    max_val = 0
    for i in combos:
        min_val = 0
        for j in range(0,len(i),2):
            min_val += min(i[j], i[j+1])
        max_val = min_val if min_val > max_val else max_val
    return max_val

# sort the list and then use list comprehension
def arraySumPair2(nums: List[int]):
    nums.sort()
    nums = nums[::2]
    return sum(nums)

# same as above but one-line soln
def arraySumPair3(nums: List[int]):
    return sum(sorted(nums)[::2])

time1a = timeit.timeit(lambda: arraySumPair1([1,4,3,2]), number=10000)
time1b = timeit.timeit(lambda: arraySumPair2([1,4,3,2]), number=10000)
time1c = timeit.timeit(lambda: arraySumPair3([1,4,3,2]), number=10000)


time2a = timeit.timeit(lambda: arraySumPair1([6,2,6,5,1,2]), number=10000)
time2b = timeit.timeit(lambda: arraySumPair2([6,2,6,5,1,2]), number=10000)
time2c = timeit.timeit(lambda: arraySumPair3([6,2,6,5,1,2]), number=10000)

time3a = timeit.timeit(lambda: arraySumPair1([6,2,6,5,1,2,0,8]), number=10000)
time3b = timeit.timeit(lambda: arraySumPair2([6,2,6,5,1,2,0,8]), number=10000)
time3c = timeit.timeit(lambda: arraySumPair3([6,2,6,5,1,2,0,8]), number=10000)

# Print the runtimes
print("Runtime (arraySumPair1):", time1a, time2a, time3a) #3 (by a LOT)
print("Runtime (arraySumPair2):", time1b, time2b, time3b) #1
print("Runtime (arraySumPair3):", time1c, time2c, time3c) #2