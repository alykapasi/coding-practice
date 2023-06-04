import timeit

# Leetcode 2089 (06/02/2023)
# Defining functions

# Brute force solution - using type switching
def isSameAfterReversals1(num: int):
    return int(str(int(str(num)[::-1]))[::-1]) == num

# Brute force solution - using arithmetic
def isSameAfterReversals2(num: int):
    reversed1 = 0
    temp = abs(num)

    while temp > 0:
        digit = temp % 10
        reversed1 = reversed1 * 10 + digit
        temp //= 10

    reversed2 = 0
    temp = reversed1

    while temp > 0:
        digit = temp % 10
        reversed2 = reversed2 * 10 + digit
        temp //= 10

    return reversed2 == num

# Check if the last char is 0 if yes return False
def isSameAfterReversals3(num: int):
        return not str(num)[-1] == '0' if num != 0 else True

# Measure the runtime using different test cases
time1a = timeit.timeit(lambda: isSameAfterReversals1(526), number=10000)
time1b = timeit.timeit(lambda: isSameAfterReversals2(526), number=10000)
time1c = timeit.timeit(lambda: isSameAfterReversals3(526), number=10000)


time2a = timeit.timeit(lambda: isSameAfterReversals1(1806564680), number=10000)
time2b = timeit.timeit(lambda: isSameAfterReversals2(1806564680), number=10000)
time2c = timeit.timeit(lambda: isSameAfterReversals3(1806564680), number=10000)

time3a = timeit.timeit(lambda: isSameAfterReversals1(0), number=10000)
time3b = timeit.timeit(lambda: isSameAfterReversals2(0), number=10000)
time3c = timeit.timeit(lambda: isSameAfterReversals3(0), number=10000)

# Print the runtimes
print("Runtime (evenOddBit1):", time1a, time2a, time3a)
print('\n')
print("Runtime (evenOddBit2):", time1b, time2b, time3b)
print('\n')
print("Runtime (evenOddBit3):", time1c, time2c, time3c)
