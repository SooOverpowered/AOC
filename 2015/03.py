def part1(data):
    line = data.rstrip()
    array = [(0, 0)]
    x, y = 0, 0
    for ins in line:
        if ins == '^':
            y += 1
        elif ins == 'v':
            y -= 1
        elif ins == '>':
            x += 1
        else:
            x -= 1
        if (x, y) not in array:
            array.append((x, y))
    return len(array)


def part2(data):
    line = data.rstrip()
    santa = [line[i] for i in range(0, len(line), 2)]
    robo = [line[i] for i in range(1, len(line), 2)]
    array = [(0, 0)]
    x, y = 0, 0
    for ins in santa:
        if ins == '^':
            y += 1
        elif ins == 'v':
            y -= 1
        elif ins == '>':
            x += 1
        else:
            x -= 1
        if (x, y) not in array:
            array.append((x, y))
    x, y = 0, 0
    for ins in robo:
        if ins == '^':
            y += 1
        elif ins == 'v':
            y -= 1
        elif ins == '>':
            x += 1
        else:
            x -= 1
        if (x, y) not in array:
            array.append((x, y))
    return len(array)
