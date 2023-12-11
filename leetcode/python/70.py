## Leetcode Problem 70 - Climbing Stairs
## Dec. 8, 2023

class Solution:
    def __init__(self):
        self.visited = {}
    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n not in self.visited:
            self.visited[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return self.visited[n]