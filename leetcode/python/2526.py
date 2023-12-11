## Leetcode Problem 2526 - Find Consecutive Integers from Data Stream
## Dec. 9, 2023

class DataStream:
    def __init__(self, value: int, k: int) -> None:
        self.v = value
        self.k = k
        self.n = 0
    
    def consec(self, num: int) -> bool:
        if self.v == num:
            self.n += 1
        else:
            self.n = 0
        return self.n >= self.k