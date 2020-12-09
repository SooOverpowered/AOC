def process_wire(instr_line):
    current_pos = [0, 0]
    for instr in instr_line.split(','):
        for _ in range(int(instr[1:])):
            current_pos[0 if instr[0] in (
                'L', 'R') else 1] += -1 if instr[0] in ('L', 'D') else 1
            yield tuple(current_pos)
def part1(data):
    wires=[list(process_wire(line)) for line in data.rstrip().split('\n')]
    intersections = set(wires[0]) & set(wires[1])
    return min(abs(x)+abs(y) for (x, y) in intersections)

def part2(data):
    wires=[list(process_wire(line)) for line in data.rstrip().split('\n')]
    intersections = set(wires[0]) & set(wires[1])
    return 2 + min(sum(wire.index(intersect) for wire in wires) for intersect in intersections)