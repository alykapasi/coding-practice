## advent of code 2015 - day 7
## september 09, 2023


with open('../input/7.txt', 'r') as f:
    data = f.read().split('\n')

instructions = {}

def get_signal(wire):
    if wire.isdigit():
        return int(wire)
    
    if wire in signals:
        return signals[wire]
    
    logic = instructions[wire]

    parts = logic.split()

    if len(parts) == 1:
        ret = get_signal(parts[0])
    elif len(parts) == 2:
        ret = ~get_signal(parts[1])
    else:
        w1, w2, op = parts[0], parts[2], parts[1]

        match(op):
            case 'AND':
                ret = get_signal(w1) & get_signal(w2)
            case 'OR':
                ret = get_signal(w1) | get_signal(w2)
            case 'LSHIFT':
                ret = get_signal(w1) << get_signal(w2)
            case 'RSHIFT':
                ret = get_signal(w1) >> get_signal(w2)

    signals[wire] = ret
    return ret

## part a
signals = {}

for line in data:
    part = line.split(' -> ')
    instructions[part[1]] = part[0]

print(get_signal('a'))

## part b
signals = {}
signal_a = get_signal('a')
signals = {}
instructions['b'] = str(signal_a)
print(get_signal('a'))