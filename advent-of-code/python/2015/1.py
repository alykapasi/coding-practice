from aocd import data, submit
from collections import Counter


## part 1a (05/30/2023)
sorted_data = Counter(data)
ans = sorted_data['('] - sorted_data[')']
submit(ans, part='a', day=1, year=2015)

## part 1b (05/30/2023)
curr_floor = 0
idx = -1
for i in data:
    idx += 1
    print(f'current floor: {curr_floor}\nidx: {idx}\n')
    if i == '(':
        curr_floor += 1
    else:
        curr_floor -= 1
    if curr_floor == -1:
        break

submit(idx+1, part='b', day=1, year=2015)
