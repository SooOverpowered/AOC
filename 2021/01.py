def part1(data):
    lines = list(map(int, data.split('\n')))
    output = 0
    for i in range(len(lines)-1):
        if lines[i] > lines[i+1]:
            output += 1
    return output


def part2(data):
    lines = list(map(int, data.split('\n')))
    output = 0
    for i in range(0, len(lines)-3):
        if lines[i] < lines[i+3]:
            output += 1
    return output
