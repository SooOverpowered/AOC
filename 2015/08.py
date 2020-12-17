def part1(data):
    lines = data.rstrip().split('\n')
    total = 0
    for line in lines:
        a = line
        total += len(line)-len(eval(line))
    return total


def part2(data):
    lines = data.rstrip().split('\n')
    total = 0
    for line in lines:
        temp = [i for i in line]
        temp2 = ['"']
        for string in temp:
            if string == '"':
                temp2.extend(['\\', '"'])
            elif string == '\\':
                temp2.extend(['\\', '\\'])
            else:
                temp2.append(string)
        temp2.append('"')
        total += len(''.join(temp2))-len(line)
    return total
