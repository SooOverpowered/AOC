import numpy as np
from scipy.ndimage.filters import convolve


def part1(data):
    data = data.rstrip().split('\n')
    x = len(data[0])
    y = len(data)
    z = 1
    weight = np.ones((3, 3, 3))
    weight[1, 1, 1] = 0
    grid = np.zeros((z, y, x), dtype=np.int32)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            state = 0 if char == '.' else 1
            grid[0, y, x] = state

    def cycle(grid, weight):
        grid = np.pad(grid, 1)
        nbrs = convolve(grid, weight, mode='wrap', cval=0)
        next_grid = np.zeros(grid.shape)
        next_grid += (grid == 1) & ((nbrs == 2) | (nbrs == 3))
        next_grid += (grid == 0) & (nbrs == 3)
        return next_grid
    for i in range(6):
        grid = cycle(grid, weight)
    return int(grid.sum())


def part2(data):
    data = data.rstrip().split('\n')
    x = len(data[0])
    y = len(data)
    z = 1
    w = 1
    weight = np.ones((3, 3, 3, 3))
    weight[1, 1, 1, 1] = 0
    grid = np.zeros((w, z, y, x), dtype=np.int32)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            state = 0 if char == '.' else 1
            grid[0, 0, y, x] = state

    def cycle(grid, weight):
        grid = np.pad(grid, 1)
        nbrs = convolve(grid, weight, mode='wrap', cval=0)
        next_grid = np.zeros(grid.shape)
        next_grid += (grid == 1) & ((nbrs == 2) | (nbrs == 3))
        next_grid += (grid == 0) & (nbrs == 3)
        return next_grid
    for i in range(6):
        grid = cycle(grid, weight)
    return int(grid.sum())
