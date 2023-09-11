## advent of code 2015 - day 5
## september 07, 2023

with open('../input/5.txt', 'r') as f:
    data = f.read().split('\n')

vowels = ['a','e','i','o','u']
illegal = ['ab', 'cd', 'pq', 'xy']

## part a
ans = 0
for i in data:
    cond3 = any([(j in i) for j in illegal])
    if cond3:
        continue
    cond2 = False
    for k in range(len(i)-1):
        if i[k] == i[k+1]: cond2 = True
    if not cond2:
        continue
    cond1 = [1  if (l in vowels) else 0 for l in i]
    ans += 1 if sum(cond1) > 2 else 0

print(ans)

## part b
ans = 0
for i in data:
    cond1 = False
    for j in range(len(i)-1):
        if i[j:j+2] in i[j+2:]:
            cond1 = True
            break
    if not cond1: continue
    cond2 = False
    for k in range(len(i)-2):
        if i[k] == i[k+2]:
            cond2 = True
            break
    ans += 1 if cond2 else 0

print(ans)