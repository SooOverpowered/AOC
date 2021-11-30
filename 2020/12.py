class Ship:
    rotation = ((1, 0), (0, -1), (-1, 0), (0, 1))

    def __init__(self, x=0, y=0, direction=0):
        self.x = x
        self.y = y
        self.direction = direction

    def change_direction(self, value, multiplier):
        self.direction += value*multiplier
        if self.direction < -4 or self.direction > 3:
            self.direction = self.direction % 4

    def forward(self, multiplier):
        directional = self.rotation[self.direction]
        self.x += directional[0]*multiplier
        self.y += directional[1]*multiplier

    def move_north(self, value):
        self.y += value

    def move_south(self, value):
        self.y -= value

    def move_east(self, value):
        self.x += value

    def move_west(self, value):
        self.x -= value

    def manhattan_distance(self):
        return abs(self.x)+abs(self.y)


class Ship2:

    def __init__(self, x=0, y=0, wx=10, wy=1, direction=0):
        self.x = x
        self.y = y
        self.wx = wx
        self.wy = wy
        self.direction = direction

    def change_direction(self, value, multiplier):
        diff_x = self.wx-self.x
        diff_y = self.wy-self.y
        for i in range(value):
            if multiplier == -1:
                tempx = diff_x
                tempy = diff_y
                diff_x = tempy*-1
                diff_y = 1*tempx
            else:
                tempx = diff_x
                tempy = diff_y
                diff_x = 1*tempy
                diff_y = tempx*-1
        self.wx = self.x+diff_x
        self.wy = self.y+diff_y

    def forward(self, multiplier):
        diff_x = self.wx-self.x
        diff_y = self.wy-self.y
        self.wx += multiplier*diff_x
        self.wy += multiplier*diff_y
        self.x += multiplier*diff_x
        self.y += multiplier*diff_y

    def move_north(self, value):
        self.wy += value

    def move_south(self, value):
        self.wy -= value

    def move_east(self, value):
        self.wx += value

    def move_west(self, value):
        self.wx -= value

    def manhattan_distance(self):
        return abs(self.x)+abs(self.y)


def part1(data):
    lines = data.rstrip().split('\n')
    lines = [[line[0], int(line[1:])] for line in lines]
    ship = Ship()
    for line in lines:
        if line[0] == 'F':
            ship.forward(line[1])
        elif line[0] == 'R':
            ship.change_direction(line[1]//90, 1)
        elif line[0] == 'L':
            ship.change_direction(line[1]//90, -1)
        elif line[0] == 'N':
            ship.move_north(line[1])
        elif line[0] == 'S':
            ship.move_south(line[1])
        elif line[0] == 'E':
            ship.move_east(line[1])
        elif line[0] == 'W':
            ship.move_west(line[1])
    return ship.manhattan_distance()


def part2(data):
    lines = data.rstrip().split('\n')
    lines = [[line[0], int(line[1:])] for line in lines]
    ship = Ship2()
    for line in lines:
        if line[0] == 'F':
            ship.forward(line[1])
        elif line[0] == 'R':
            ship.change_direction(line[1]//90, 1)
        elif line[0] == 'L':
            ship.change_direction(line[1]//90, -1)
        elif line[0] == 'N':
            ship.move_north(line[1])
        elif line[0] == 'S':
            ship.move_south(line[1])
        elif line[0] == 'E':
            ship.move_east(line[1])
        elif line[0] == 'W':
            ship.move_west(line[1])
    return ship.manhattan_distance()
