class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(0, 1000)] for y in range(0, 1000)]

    def draw_line(self, start, end):
        if start.x == end.x:
            if start.y < end.y:
                for i in range(start.y, end.y+1):
                    self.grid[i][start.x] += 1
            else:
                self.draw_line(end, start)
        elif start.y == end.y:
            if start.x < end.x:
                for i in range(start.x, end.x+1):
                    self.grid[start.y][i] += 1
            else:
                self.draw_line(end, start)
        # Uncomment below for part 2
        else:
            if start.x < end.x:
                if start.y < end.y:
                    x = start.x
                    y = start.y
                    while x <= end.x and y <= end.y:
                        self.grid[y][x] += 1
                        x += 1
                        y += 1
                else:
                    x = start.x
                    y = start.y
                    while x <= end.x and y >= end.y:
                        self.grid[y][x] += 1
                        x += 1
                        y -= 1
            else:
                self.draw_line(end, start)

    def overlap_count(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if cell > 1:
                    count += 1
        return count


def part1(data):
    lines = data.split('\n')
    grid = Grid()
    for line in lines:
        start, end = line.split(' -> ')
        start = Point(int(start.split(',')[0]), int(start.split(',')[1]))
        end = Point(int(end.split(',')[0]), int(end.split(',')[1]))
        grid.draw_line(start, end)
    return grid.overlap_count()


def part2(data):
    lines = data.split('\n')
    lines = data.split('\n')
    grid = Grid()
    for line in lines:
        start, end = line.split(' -> ')
        start = Point(int(start.split(',')[0]), int(start.split(',')[1]))
        end = Point(int(end.split(',')[0]), int(end.split(',')[1]))
        grid.draw_line(start, end)
    return grid.overlap_count()


if __name__ == "__main__":
    import runner
    runner.run(day=5)
