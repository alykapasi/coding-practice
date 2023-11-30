## Leetcode 371 - Sum of Two Integers
## Nov. 29, 2023

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) > 0:
            c = a & b
            a ^= b
            b = c << 1
        return a & mask if b > mask else a