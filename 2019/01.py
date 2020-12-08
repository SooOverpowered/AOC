def part1(data):
    lines=data.rstrip().split('\n')
    output = 0
    for line in lines:
        output += int(line)//3-2
    return output


def part2(data):
    lines=data.rstrip().split('\n')
    output = 0
    for line in lines:
        curr = int(line)//3-2
        while curr > 0:
            output += curr
            curr = curr//3-2
    return output