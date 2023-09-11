## advent of code 2015 - day 4
## september 06, 2023

import hashlib

with open('../input/4.txt', 'r') as f:
    data = f.read()

## part a
for i in range(1000000):
    hashed = hashlib.md5((data + str(i)).encode()).hexdigest()
    if hashed[:5] == '00000':
        print(i)
        break

## part b
for i in range(10000000):
    hashed = hashlib.md5((data + str(i)).encode()).hexdigest()
    if hashed[:6] == '000000':
        print(i)
        break