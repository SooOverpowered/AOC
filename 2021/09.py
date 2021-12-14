import numpy as np


def part1(data):
    lines = [list(map(int, list(line))) for line in data.split('\n')]
    lines = np.array(lines)
    lines = np.pad(lines, pad_width=1, mode='constant', constant_values=9)
    output = 0
    for r, row in enumerate(lines):
        if 0 < r < len(lines)-1:
            for c, height in enumerate(row):
                if 0 < c < len(row)-1:
                    if height < min([lines[r-1, c], lines[r+1, c], lines[r, c-1], lines[r, c+1]]):
                        output += height+1
    return output


def calc_basin(lines, r, c):
    basin = {(r, c)}
    for a,b, in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
        if lines[a,b] > lines[r,c] and lines[a,b]<9:
            basin |= calc_basin(lines, a, b)
    return basin

def part2(data):
    lines = [list(map(int, list(line))) for line in data.split('\n')]
    lines = np.array(lines)
    lines = np.pad(lines, pad_width=1, mode='constant', constant_values=9)
    basins = []
    for r, row in enumerate(lines):
        if 0 < r < len(lines)-1:
            for c, height in enumerate(row):
                if 0 < c < len(row)-1:
                    if height < min([lines[r-1, c], lines[r+1, c], lines[r, c-1], lines[r, c+1]]):
                        basins.append(len(calc_basin(lines, r, c)))
    basins.sort(reverse=True)
    return basins[0]*basins[1]*basins[2]


if __name__ == '__main__':
    import runner
    runner.run(day=9)
