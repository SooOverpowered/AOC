def part1(data):
    lines=data.split('\n')
    depth=0
    horiz=0
    for line in lines:
        command, value = line.split(' ')
        if command == 'forward':
            horiz += int(value)
        elif command == 'up':
            depth -= int(value)
        elif command == 'down':
            depth += int(value)
    return horiz*depth

def part2(data):
    lines=data.split('\n')
    depth=0
    horiz=0
    aim=0
    for line in lines:
        command, value = line.split(' ')
        if command == 'forward':
            horiz += int(value)
            depth += aim*int(value)
        elif command == 'up':
            aim -= int(value)
        elif command == 'down':
            aim += int(value)
    return horiz*depth