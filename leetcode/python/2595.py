import timeit

# Leetcode 2595 (06/01/2023)
# Defining functions

# brute force
def evenOddBit1(n):
    binary = bin(n)[2:]
    n_bits = len(binary)
    ans = [0,0]
    for i in range(n_bits):
        if binary[i] == '1':
            ans[(n_bits-i-1) % 2] += 1

    return ans

# using bit manipulation
def evenOddBit2(n):
    n_bits = len(bin(n)) - 2
    ans = [0,0]
    for i in range(n_bits):
        if n & (1 << i):
            ans[i % 2] += 1

    return ans

# Measure the runitme using different test cases
time1a = timeit.timeit(lambda: evenOddBit1(17), number=10000)
time1b = timeit.timeit(lambda: evenOddBit2(17), number=10000)

time2a = timeit.timeit(lambda: evenOddBit1(2), number=10000)
time2b = timeit.timeit(lambda: evenOddBit2(2), number=10000)

time3a = timeit.timeit(lambda: evenOddBit1(654), number=10000)
time3b = timeit.timeit(lambda: evenOddBit2(654), number=10000)

# Print the runtimes
print("Runtime (evenOddBit1):", time1a, time2a, time3a)
print("Runtime (evenOddBit2):", time1b, time2b, time3b)