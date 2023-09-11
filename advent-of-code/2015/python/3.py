## advent of code 2015 - day 3
## september 05, 2023

with open('../input/3.txt', 'r') as f:
    data = f.read()

## part a
visited = set()
coords = [0,0]
visited.add(tuple(coords))

for i in data:
    match i:
        case '>':
            coords[0] += 1
        case '<':
            coords[0] -= 1
        case '^':
            coords[1] += 1
        case 'v':
            coords[1] -= 1
    visited.add(tuple(coords))

print(len(visited))

 ## part b
visited = set()
santa = [0,0]
robot = [0,0]
visited.add(tuple(santa))
is_santa = True

for i in data:
    if is_santa:
        match i:
            case '>':
                santa[0] += 1
            case '<':
                santa[0] -= 1
            case '^':
                santa[1] += 1
            case 'v':
                santa[1] -= 1
        visited.add(tuple(santa))
    else:
        match i:
            case '>':
                robot[0] += 1
            case '<':
                robot[0] -= 1
            case '^':
                robot[1] += 1
            case 'v':
                robot[1] -= 1
        visited.add(tuple(robot))
    is_santa = not is_santa

print(len(visited))