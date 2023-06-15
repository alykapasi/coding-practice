from aocd import data, submit
import numpy as np

## part 6a
grid = np.zeros((1000, 1000))
split_data = data.split('\n')

for i in split_data:
    line = i.split(' ')
    if len(line) == 5:
        if line[1] == 'on':
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            #print(f'x1,x2 = {x1,x2}, y1,y2 = {y1,y2}')
            grid[x1:x2+1, y1:y2+1] = 1
        elif line[1] == 'off':
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            #print(f'x1,x2 = {x1,x2}, y1,y2 = {y1,y2}')
            grid[x1:x2+1, y1:y2+1] = 0
    elif len(line) == 4:
        x1, y1 = map(int, line[1].split(','))
        x2, y2 = map(int, line[3].split(','))
        #print(f'x1,x2 = {x1,x2}, y1,y2 = {y1,y2}')
        grid[x1:x2+1, y1:y2+1] = 1 - grid[x1:x2+1, y1:y2+1]

ans = int(np.sum(grid))

submit(ans, part='a', day=6, year=2015)

## part 6b
grid = np.zeros((1000, 1000))
split_data = data.split('\n')

for i in split_data:
    line = i.split(' ')
    if len(line) == 5:
        if line[1] == 'on':
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            grid[x1:x2+1, y1:y2+1] += 1
        elif line[1] == 'off':
            x1, y1 = map(int, line[2].split(','))
            x2, y2 = map(int, line[4].split(','))
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0
    elif len(line) == 4:
        x1, y1 = map(int, line[1].split(','))
        x2, y2 = map(int, line[3].split(','))
        grid[x1:x2+1, y1:y2+1] += 2

ans = int(np.sum(grid))

submit(ans, part='b', day=6, year=2015)