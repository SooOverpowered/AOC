def part1(data):
    blocks = data.split('\n\n')
    elfs = [block.split('\n') for block in blocks]
    calories = []
    for elf in elfs:
        calories.append(sum([int(line) for line in elf]))
    return max(calories)


def part2(data):
    blocks = data.split('\n\n')
    elfs = [block.split('\n') for block in blocks]
    calories = []
    for elf in elfs:
        calories.append(sum([int(line) for line in elf]))
    calories.sort(reverse=True)
    return sum(calories[0:3])
