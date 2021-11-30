def part1(data):
    line=[int(num) for num in data.rstrip().split(',')]
    curr = 0
    while curr < len(line):
        if line[curr] == 1:
            first = line[curr+1]
            second = line[curr+2]
            pos = line[curr+3]
            total = line[first]+line[second]
            line[pos] = total
            curr += 4
        elif line[curr] == 2:
            first = line[curr+1]
            second = line[curr+2]
            pos = line[curr+3]
            total = line[first]*line[second]
            line[pos] = total
            curr += 4
        elif line[curr] == 99:
            break
    return line[0]


def test(a, b,data):
    line=[int(num) for num in data.rstrip().split(',')]
    blocks = [line[i:i+4] for i in range(0, len(line), 4)]
    blocks[0][1], blocks[0][2] = a, b
    for block in blocks:
        if block[0] == 1:
            first = block[1]
            second = block[2]
            pos = block[3]
            total = blocks[first//4][first %4]+blocks[second//4][second % 4]
            blocks[pos//4][pos % 4] = total
        elif block[0] == 2:
            first = block[1]
            second = block[2]
            pos = block[3]
            total = blocks[first//4][first %4]*blocks[second//4][second % 4]
            blocks[pos//4][pos % 4] = total
        elif block[0] == 99:
            break
    return blocks[0][0]


def part2(data):
    for i in range(0, 100):
        for j in range(0, 100):
            if test(i, j,data) == 19690720:
                return 100*i+j