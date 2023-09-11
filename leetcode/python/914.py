## leetcode problem 914
## https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

## september 05, 2023

from typing import List

def hasGroupSizeX(deck: List[int]) -> bool:
    vals = list(set(deck))
    check = deck.count(vals[0])
    ans = True
    for i in range(1, len(vals)):
        if check != deck.count(vals[i]):
            ans = False
            break
    return ans

print(hasGroupSizeX([1,2,3,4,4,3,2,1]))
print(hasGroupSizeX([1,1,1,2,2,2,3,3]))