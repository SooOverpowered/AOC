from collections import defaultdict


class Cycle:
    def __init__(self, length, curr):
        self.length = length
        self.curr = curr-1

    def move(self, steps):
        self.curr = self.curr + steps
        if self.curr >= self.length:
            self.curr = self.curr % self.length

    def roll(self):
        output = self.curr+1
        self.curr += 1
        if self.curr >= self.length:
            self.curr = self.curr % self.length
        return output


def part1(data):
    p1, p2 = data.split('\n')
    p1_score = 0
    p2_score = 0
    p1 = Cycle(10, int(p1))
    p2 = Cycle(10, int(p2))
    dice = Cycle(100, 1)
    count = 0
    while True:
        steps = sum([dice.roll() for _ in range(3)])
        count += 3
        p1.move(steps)
        p1_score += p1.curr+1
        if p1_score >= 1000:
            return p2_score*count
        else:
            steps = sum([dice.roll() for _ in range(3)])
            count += 3
            p2.move(steps)
            p2_score += p2.curr+1
            if p2_score >= 1000:
                return p1_score*count


def part2(data):
    pass


if __name__ == '__main__':
    import runner
    runner.run(day=21)
