## Leetcode Problem 1422 - 
## Dec. 5, 2023

class Solution:
    def maxScore(self, s: str) -> int:
        zero = 1 if s[0] == '0' else 0
        one = s[1:].count('1')
        score = zero + one

        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            score = max(score, zero + one)
        
        return score
    
    def maxScore1(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            lhs, rhs = s[:i], s[i:]
            score = max(score, lhs.count('0') + rhs.count('1'))
        return score
    
    def maxScore2(self, s: str) -> int:
        return max([s[:i].count('0') + s[i:].count('1') for i in range(1, len(s))])