def part1(data):
    lines = data.rstrip().split('\n')
    lines = [line.split('x') for line in lines]
    total = 0
    for line in lines:
        line = [int(i) for i in line]
        line = sorted(line)
        total += line[0]*line[1]*3+line[1]*line[2]*2+line[2]*line[0]*2
    return total


def part2(data):
    lines = data.rstrip().split('\n')
    lines = [line.split('x') for line in lines]
    total = 0
    for line in lines:
        line = [int(i) for i in line]
        line = sorted(line)
        total += 2*line[0]+2*line[1]+line[1]*line[2]*line[0]
    return total
