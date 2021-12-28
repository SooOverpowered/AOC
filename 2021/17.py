def part1(data):
    x_bound,y_bound = data.split(',')
    x_bound=list(map(int, x_bound.split('..')))
    y_bound=list(map(int, y_bound.split('..')))
    return abs(y_bound[0])*abs(y_bound[0]+1)/2


def part2(data):
    pass

if __name__ == '__main__':
    import runner
    runner.run(day=17)