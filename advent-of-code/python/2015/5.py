from aocd import data, submit
import re

## part 5a
split_data = data.split('\n')

## condition1 - return True if there are atleast 3 vowels (can repeat vowels)
def cond1(s: str):
    vowels = ['a','e','i','o','u']
    ans = [1 for i in s if i in vowels]
    return sum(ans) >= 3

## condition2 - check if there are 2 same letters one after another
## return True if there are 2 same consecutive characters
def cond2(s: str):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

## condition3 - check if invalid combinations exist in the string
## return True if none are in string
def cond3(s: str):
    for i in ['ab','cd','pq','xy']:
        if i in s:
            return False
    return True

count = 0    
ans = sum([1 for i in split_data if (cond1(i) and cond2(i) and cond3(i)) == True])
#submit(ans, part='a', day=5, year=2015)

## part 5b
## condition 1(NEW) - if there are 2 consecutive characters that repeat with some character in between
def cond1new(s):
    if not re.search(r'(..).*\1', s):
        return False

    if not re.search(r'(.).\1', s):
        return False
    return True

## condition 2(NEW) - if there is a repeating character with a different
## character intbetween return True
def cond2new(s: str):
    return bool(re.search(r'(.).\1', s))

ans = sum([1 for i in split_data if (cond1new(i) and cond2new(i)) == True])
submit(ans, part='b', day=5, year=2015)