## advent of code 2015 - day 6
## september 08, 2023

import numpy as np

with open('../input/6.txt', 'r') as f:
    data = f.read().split('\n')

## part a
grid = np.zeros((1000,1000))

for i in data:
    line = i.split(' ')
    if len(line) == 4:
        start = line[1].split(',')
        stop = line[-1].split(',')

        for x in range(int(start[0]), int(stop[0]) + 1):
            for y in range(int(start[1]), int(stop[1]) + 1):
                grid[y,x] = 1 - grid[y,x]
    else:
        start = line[2].split(',')
        stop = line[-1].split(',')

        if line[1] == 'on':
            grid[int(start[1]):int(stop[1]) + 1, int(start[0]):int(stop[0]) + 1] = 1
        if line[1] == 'off':
            grid[int(start[1]):int(stop[1]) + 1, int(start[0]):int(stop[0]) + 1] = 0

print(int(np.sum(grid)))

## part b
grid = np.zeros((1000,1000))

for i in data:
    line = i.split(' ')
    stop = line[-1].split(',')
    
    if len(line) == 4:
        start = line[1].split(',')

        grid[int(start[1]):int(stop[1]) + 1, int(start[0]):int(stop[0]) + 1] += 2
    else:
        start = line[2].split(',')

        if line[1] == 'on':
            grid[int(start[1]):int(stop[1]) + 1, int(start[0]):int(stop[0]) + 1] += 1
        if line[1] == 'off':
            grid[int(start[1]):int(stop[1]) + 1, int(start[0]):int(stop[0]) + 1] -= 1
            grid[grid < 0] = 0

print(int(np.sum(grid)))