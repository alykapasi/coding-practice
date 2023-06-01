from aocd import data, submit

## part 2a (05/31/2023)
sorted_data = data.split('\n')
ans = 0

for i in sorted_data:
    dims = i.split('x')
    l,w,h = int(dims[0]),int(dims[1]),int(dims[2])
    area = 2*((l*w)+(w*h)+(l*h))
    slack = min(l*w, w*h, l*h)
    ans += area + slack

submit(ans, part='a', day=2, year=2015)

## part 2b (05/31/2023)
ans = 0

for i in sorted_data:
    dims = i.split('x')
    l,w,h = int(dims[0]),int(dims[1]),int(dims[2])
    ribbon = 2 * min(l+w, w+h, l+h) + (l*w*h)
    ans += ribbon

submit(ans, part='b', day=2, year=2015)
