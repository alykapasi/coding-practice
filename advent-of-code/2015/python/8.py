## advent of code 2015 - day 8
## september 10, 2023

with open('../input/8.txt', 'r') as f:
    data = f.read().split('\n')

len_code = 0
len_memory = 0

## part a
for i in data:
    len_code += len(i)
    len_memory += len(eval(i))
print(len_code - len_memory)

## part b
ans = 0

for i in data:
    count = i.count('\\') + i.count('"') + 2
    ans += count
print(ans)