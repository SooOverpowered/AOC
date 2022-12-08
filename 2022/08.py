import numpy as np
def part1(data):
    grid = np.array([list(map(int, line)) for line in data.split('\n')])
    width = len(grid[0])
    height = len(grid)
    grid_size = width*height
    invis = 0
    for row in range(height):
        for col in range(width):
            if 0<row<height-1 and 0<col<width-1:
                tree = grid[row, col]
                if max(grid[row, 0:col]) >= tree and tree <= max(grid[row, col+1:]) and max(grid[0:row, col]) >= tree and tree <= max(grid[row+1:, col]):
                    invis+=1
    return grid_size-invis

def calc_score(value, arr, reversed):
    if reversed:
        arr = arr[::-1]
    for i, v in enumerate(arr):
        if v >= value:
            return i+1
    return len(arr)
def part2(data):
    grid = np.array([list(map(int, line)) for line in data.split('\n')])
    width = len(grid[0])
    height = len(grid)
    max_score = 0
    for row in range(height):
        for col in range(width):
            if 0<row<height-1 and 0<col<width-1:
                left_score = calc_score(grid[row, col], grid[row, 0:col], True)
                right_score = calc_score(grid[row, col], grid[row, col+1:], False)
                up_score = calc_score(grid[row, col], grid[0:row, col], True)
                down_score = calc_score(grid[row, col], grid[row+1:, col], False)
                scenic_score = left_score * right_score * up_score * down_score
                if scenic_score > max_score:
                    max_score = scenic_score
    return max_score