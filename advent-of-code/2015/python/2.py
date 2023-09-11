## advent of code 2015 - day 2
## september 04, 2023

with open('../input/2.txt', 'r') as f:
    data = f.read()
data = data.split('\n')

## part a
ans = 0
for i in data:
    s = i.split('x')
    l,w,h = int(s[0]), int(s[1]), int(s[2])
    areas = l*w, w*h, l*h
    ans += 2 * sum(areas) + min(areas)
print(ans)

## part b
ans = 0
for i in data:
    s = i.split('x')
    l,w,h = int(s[0]), int(s[1]), int(s[2])
    bow = l*w*h
    ribbon = 2 * (l + w + h - max(l,w,h))
    ans += bow + ribbon
print(ans)