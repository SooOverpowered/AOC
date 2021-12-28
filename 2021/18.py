def reduce(data):
    

def part1(data):
    lines = [eval(line) for line in data.split('/n')]
    output = lines[0]
    for line in lines[1::]:
        output = [output, line]
        output = reduce(output)


def part2(data):
    pass


if __name__ == '__main__':
    import runner
    runner.run(day=18)
