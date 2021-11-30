def part1(data):
    line = [ins for ins in data.rstrip()]
    opening = len([ins for ins in line if ins == '('])
    closing = len([ins for ins in line if ins == ')'])
    return opening-closing


def part2(data):
    line = [ins for ins in data.rstrip()]
    level = 0
    for i in range(len(line)):
        if line[i] == '(':
            level += 1
        else:
            level -= 1
        if level == -1:
            return i+1
