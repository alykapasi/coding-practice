from aocd import data, submit

## part 7a

instructions = data
signals = wire_instructions = {}

def get_signal(wire):
    if wire in signals:
        return signals[wire]
    
    if wire.isdigit():
        return int(wire)
    
    instruction = wire_instructions[wire]
    
    parts = instruction.split()
    if len(parts) == 1:
        signal = get_signal(parts[0])
    elif len(parts) == 2:
        signal = ~get_signal(parts[1])
    else:
        wire1 = parts[0]
        operator = parts[1]
        wire2 = parts[2]
        
        if operator == 'AND':
            signal = get_signal(wire1) & get_signal(wire2)
        elif operator == 'OR':
            signal = get_signal(wire1) | get_signal(wire2)
        elif operator == 'LSHIFT':
            signal = get_signal(wire1) << int(wire2)
        elif operator == 'RSHIFT':
            signal = get_signal(wire1) >> int(wire2)
    
    signals[wire] = signal
    return signal

for line in instructions.split('\n'):
    parts = line.split(' -> ')
    wire_instructions[parts[1]] = parts[0]

ans = get_signal('a')
# submit(ans, part='a', day=7, year=2015)

## part 7b
signals = {}
sig_a = get_signal('a')
signals = {}
wire_instructions['b'] = str(sig_a)
new_sig = get_signal('a')
submit(new_sig, part='b', day=7, year=2015)