## Leetcode Problem 6 - ZigZag Conversion
## Dec. 10, 2023

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        ans = [""] * numRows
        i, vert = 0, True

        for c in s:
            ans[i] += c
            
            if not i: vert = True
            elif i == numRows - 1: vert = False

            if vert: i += 1
            else: i -= 1

        return "".join(ans)