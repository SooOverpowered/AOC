from statistics import median


def part1(data):
    numbers = list(map(int, data.split(',')))
    return min(sum(abs(num-goal) for num in numbers) for goal in range(min(numbers), max(numbers)+1))


def part2(data):
    numbers = list(map(int, data.split(',')))
    return min(sum((abs(num - goal) * (abs(num - goal) + 1)) // 2 for num in numbers) for goal in range(min(numbers), max(numbers)+1))


if __name__ == '__main__':
    import runner
    runner.run(day=7)