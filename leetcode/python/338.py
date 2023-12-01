## Leetcode 338 - Counting Bits
## Dec. 1, 2023

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            ans.append(ans[i // 2] + (i % 2))
        
        return ans