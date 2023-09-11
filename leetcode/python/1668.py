## leetcode problem 1668
## https://leetcode.com/problems/maximum-repeating-substring/

## september 04, 2023

def maxRepeating(sequence: str, word: str) -> int:
    i = 0
    while word * i in sequence:
        i += 1
    return i - 1

print(maxRepeating("ababc", "ab"))
print(maxRepeating("ababc", "ba"))
print(maxRepeating("ababc", "ac"))

