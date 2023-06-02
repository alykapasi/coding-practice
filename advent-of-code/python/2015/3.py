from aocd import data, submit
from collections import namedtuple

def trackMove(x: int, y: int, dirc: str):
    match(dirc):
        case '>':
            x += 1
        case '^':
            y += 1
        case '<':
            x -= 1
        case 'v':
            y -= 1
    return x,y

## part 3a
x = y = 0
visited = [(0,0)]

for d in data:
    x,y = trackMove(x, y, d)
    visited.append((x,y))
ans = len(set(visited))

#submit(ans, part='a', day=3, year=2015)

## part 3b
santa = robo = [(0,0)]
sx = sy = rx = ry = 0
is_santa = True

for d in data:
    if is_santa:
        sx, sy = trackMove(sx, sy, d)
        santa.append((sx, sy))
    else:
        rx, ry = trackMove(rx, ry, d)
        robo.append((rx,ry))
    is_santa = not is_santa

ans = len(set(santa + robo))
submit(ans, part='b', day=3, year=2015)