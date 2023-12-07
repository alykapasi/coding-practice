## Leetcode Problem 957 - Prison Cells After N Days
## Dec. 6, 2023

from typing import List

def xnor(a, b):
    return int(not a^b)

def get_cycle(cells):
    cycle = {}
    for i in range(14):
        curr = []
        for j in range(1, len(cells) - 1):
            curr.append(xnor(cells[j - 1], cells[j + 1]))
        cells = [0] + curr + [0]
        cycle[i] = cells
    return cycle

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cycle = get_cycle(cells)
        return cycle[(n - 1) % 14]

    def prisonAfterNDays1(self, cells: List[int], n: int) -> List[int]:
        if n == 0:
            return cells
        curr = [0]
        for i in range(1, len(cells) - 1):
            temp = 1 if cells[i-1] == cells[i+1] else 0
            curr.append(temp)
        curr.append(0)
        return self.prisonAfterNDays1(curr, n-1)
    
s = Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)
print(s)