## advent of code 2015 - day 1
## september 03, 2023

with open('../input/1.txt', 'r') as f:
    data = f.read()

## part a
curr_floor = 0
ans = [1 if i == '(' else -1 for i in data]
print(sum(ans))

##part b
curr_floor = counter = 0
for i in data:
    if i == '(':
        curr_floor += 1
    else:
        curr_floor -= 1
    counter += 1
    if curr_floor < 0:
        break
print(counter)