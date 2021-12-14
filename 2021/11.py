from importlib import find_loader
from re import S


class Selector:
    def __init__(self, grid, r=0, c=0):
        self.grid = grid
        self.flash_count = 0
        self.r = r
        self.c = c
        self.flashed = set()
        self.steps=1
        self.done = False

    def find_adjacent(self, r, c):
        adjacent_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1),
                          (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
        temp=[]
        for coord in adjacent_cells:
            if 0<=coord[0]<=9 and 0<=coord[1]<=9:
                temp.append(coord)
        return temp

    def check_cell(self, r, c):
        self.grid[r][c] += 1
        if self.grid[r][c] > 9 and (r, c) not in self.flashed:
            self.flashed.add((r, c))
            for cell in self.find_adjacent(r, c):
                self.check_cell(cell[0], cell[1])

    def refresh_flashed(self):
        if len(self.flashed) ==100:
            print(self.steps)
            self.done = True
        for cell in self.flashed:
            self.flash_count += 1
            self.grid[cell[0]][cell[1]] = 0
        self.flashed = set()

    def step(self):
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                self.check_cell(r, c)
        self.refresh_flashed()
        self.steps+=1


def part1(data):
    lines = data.split('\n')
    lines = [list(map(int, line)) for line in lines]
    selector = Selector(lines)
    for step in range(100):
        selector.step()
    return selector.flash_count


def part2(data):
    lines = data.split('\n')
    lines = [list(map(int, line)) for line in lines]
    selector = Selector(lines)
    while selector.done == False:
        selector.step()
    return selector.steps-1


if __name__ == '__main__':
    import runner
    runner.run(day=11)
