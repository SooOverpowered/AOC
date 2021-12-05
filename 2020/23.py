class Game:
    def __init__(self, cups):
        self.cups = cups
        self.current = self.cups[0]
        self.low = min(self.cups)
        self.high = max(self.cups)
        self.cups = dict(zip(self.cups, self.cups[1:]+ [self.cups[0]]))

    def move(self):
        temp = [self.cups[self.current]]
        temp.append(self.cups[temp[0]])
        temp.append(self.cups[temp[-1]])
        dest = self.current -1
        while dest < self.low or dest in temp:
            dest -= 1
            if dest < self.low:
                dest = self.high
        self.cups[self.current] = self.cups[temp[-1]]
        self.cups[temp[-1]] = self.cups[dest]
        self.cups[dest] = temp[0]
        self.current = self.cups[self.current]


def part1(data):
    line = data.rstrip()
    line = [int(i) for i in line]
    game = Game(line)
    for i in range(100):
        game.move()
    label = [game.cups[1]]
    while label[-1] != 1:
        label.append(game.cups[label[-1]])
    return ''.join(map(str,label))

def part2(data):
    line = data.rstrip()
    line = [int(i) for i in line]
    line.extend(range(10, 1000001))
    game = Game(line)
    for i in range(10000000):
        game.move()
    return game.cups[1]*game.cups[game.cups[1]]

if __name__ == "__main__":
    import runner
    runner.run(day=23)
