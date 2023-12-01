## Leetcode 338 - Reverse Bits
## Dec. 1, 2023

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans <<= 1
            if n & 1:
                ans |= 1
            n >>= 1
        return ans