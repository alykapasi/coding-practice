import timeit
from typing import List

# Leetcode 2185 (05/30/2023)
# Defining functions

# brute force algorithm -> splice the word and check if the splice == pref
def prefixCount1(words: List[str], pref: str):
    i = 0
    pref_length = len(pref)
    for word in words:
        if word[:pref_length] == pref:
            i += 1
    return i

# use list comprehension and add the array to find match amount
def prefixCount2(words: List[str], pref: str):
    return sum([1 for word in words if word[:len(pref)] == pref])

# improve the speed by using startswith which involves less overhead than splicing
def prefixCount3(words: List[str], pref: str):
    return sum([1 for word in words if word.startswith(pref)])

# since the 1st solution was the fastest -> improve speed by changing splice to startswith()
def prefixCount4(words: List[str], pref: str):
    i = 0
    for word in words:
        if word.startswith(pref):
            i += 1
    return i

# Test your functions and measure their runtimes
words = ['prefix', 'preface', 'preference', 'apple', 'application']
pref = 'pre'

# Measure the runtime of prefixCount1
time1 = timeit.timeit(lambda: prefixCount1(words, pref), number=10000)

# Measure the runtime of prefixCount2
time2 = timeit.timeit(lambda: prefixCount2(words, pref), number=10000)

# Measure the runtime of prefixCount3
time3 = timeit.timeit(lambda: prefixCount3(words, pref), number=10000)

# Measure the runtime of prefixCount3
time4 = timeit.timeit(lambda: prefixCount4(words, pref), number=10000)

# Print the runtimes
print("Runtime for prefixCount1:", time1) #2
print("Runtime for prefixCount2:", time2) #4
print("Runtime for prefixCount3:", time3) #3
print("Runtime for prefixCount4:", time4) #1
