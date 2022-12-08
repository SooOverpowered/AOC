def part1(data):
    lines = data.split("\n")
    result = 0
    for line in lines:
        pairs = [list(map(int, d.split("-"))) for d in line.split(",")]
        x1, x2, y1, y2 = pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1]
        if (x1 <= x2 and y1 >= y2) or (x1 >= x2 and y1 <= y2):
            result += 1
    return result


def part2(data):
    lines = data.split("\n")
    result = 0
    for line in lines:
        pairs = [list(map(int, d.split("-"))) for d in line.split(",")]
        x1, x2, y1, y2 = pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1]
        if (x1 <= y2 and y1 >= x2):
            result += 1
    return result
