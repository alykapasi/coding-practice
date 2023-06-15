import timeit
from typing import List

# Leetcode 2089 (06/02/2023)
# Defining functions

# Brute force solution
def targetIndices1(nums: List[int], target: int):
    ans = []
    nums = sorted(nums)
    for i in range(len(nums)):
        ans.append(i) if nums[i] == target else None
    return ans

# minor improvement using enumerate and break when item > target
def targetIndices2(nums: List[int], target: int):
    ans = []
    for i, n in enumerate(sorted(nums)):
        if n == target:
            ans.append(i)
        elif(n > target):
            break
    return ans

# Test your functions and measure their runtimes
test = [1,2,5,2,3]

# Measure runtime of case 1
time1a = timeit.timeit(lambda: targetIndices1(test, 2), number=10000)
time1b = timeit.timeit(lambda: targetIndices2(test, 2), number=10000)

# Measure runtime of case 1
time2a = timeit.timeit(lambda: targetIndices1(test, 3), number=10000)
time2b = timeit.timeit(lambda: targetIndices2(test, 3), number=10000)

# Measure runtime of case 1
time3a = timeit.timeit(lambda: targetIndices1(test, 5), number=10000)
time3b = timeit.timeit(lambda: targetIndices2(test, 5), number=10000)

# Print the runtimes
print("Runtime (targetIndices1):", time1a, time2a, time3a) #2
print("Runtime (targetIndices2):", time1b, time2b, time3b) #1