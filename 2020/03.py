def part1(data):
    lines = data.rstrip().split('\n')
    count = 0
    x = 0
    for line in lines:
        if line[x] == '#':
            count += 1
        x += 3
        if x > len(line)-1:
            x = x-len(line)
    return count


def part2(data):
    lines = data.rstrip().split('\n')
    inc = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    count = 0
    output = 1
    x = 0
    y = 0
    for i in inc:
        while y < len(lines):
            if lines[y][x] == '#':
                count += 1
            x += i[0]
            if x > len(lines[y])-1:
                x = x-len(lines[y])
            y += i[1]
        x = 0
        y = 0
        output = output*count
        count = 0
    return output