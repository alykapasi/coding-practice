import timeit

# Leetcode 1464 (05/31/2023)
# Defining functions

# Brute force solution - check the entire list
def maxProduct1(nums):
    max1 = max2 = float('-inf')

    for num in nums:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    return (max1 - 1) * (max2 - 1)


# Sort the array, get the product of first 2 sorted
def maxProduct2(nums):
    nums = sorted(nums, reverse=True)
    return (nums[0] - 1) * (nums[1] - 1)

# Test cases
nums1 = [3, 4, 5, 2]
nums2 = [1, 5, 4, 5]
nums3 = [3, 7]

# Measure the runtime of maxProduct1
time1a = timeit.timeit(lambda: maxProduct1(nums1), number=10000)
time1b = timeit.timeit(lambda: maxProduct2(nums1), number=10000)

# Measure the runtime of maxProduct2
time2a = timeit.timeit(lambda: maxProduct1(nums2), number=10000)
time2b = timeit.timeit(lambda: maxProduct2(nums2), number=10000)

# Measure the runtime of maxProduct3
time3a = timeit.timeit(lambda: maxProduct1(nums3), number=10000)
time3b = timeit.timeit(lambda: maxProduct2(nums3), number=10000)

# Print the runtimes
print("Runtime (maxProduct1):", time1a, time2a, time3a)
print("Runtime (maxProduct2):", time1b, time2b, time3b)

