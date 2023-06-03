from aocd import data, submit
from hashlib import md5

## part 4a
for i in range(1000000):
    h = md5((data + str(i)).encode()).hexdigest()
    if h[:5] == '00000':
        break

submit(i, part='a', day=4, year=2015)

## 4b
for i in range(100000000):
    h = md5((data + str(i)).encode()).hexdigest()
    if h[:6] == '000000':
        break

submit(i, part='b', day=4, year=2015)
