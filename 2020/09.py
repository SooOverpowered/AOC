from itertools import combinations


def part1(data):
    lines = [int(num) for num in data.rstrip().split('\n')]
    for i in range(25, len(lines)):
        sums = []
        for combi in combinations(lines[i-25:i], 2):
            sums.append(sum(combi))
        if lines[i] not in sums:
            return lines[i]


def part2(data):
    lines = [int(num) for num in data.rstrip().split('\n')]
    processed = [line for line in lines if line < 217430975]
    length = 2
    while length < len(processed)-length:
        for i in range(len(processed)):
            if sum(processed[i:i+length]) == 217430975:
                return min(processed[i:i+length])+max(processed[i:i+length])
        length += 1
