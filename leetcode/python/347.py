## Leetcode Problem 374 - Guess Number Lower or Higher
## Dec. 8, 2023

num = 0

def guess(guess: int) -> int:
    if guess == num:
        return 0
    elif guess > num:
        return -1
    else:
        return 1
    
class Solution:
    def guessNumber(self, n: int) -> int:
        min_val, max_val = 1, n
        while min_val < max_val:
            mid_val = (min_val + max_val) // 2
            ret_val = guess(mid_val)

            if ret_val == 0:
                return mid_val
            elif ret_val > 0:
                min_val = mid_val + 1
            else:
                max_val = mid_val - 1
        
        return max_val