## Leetcode 191 - Number of 1 Bits
## Nov. 30, 2023

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += (n & 1)
            n >>= 1
        return ans