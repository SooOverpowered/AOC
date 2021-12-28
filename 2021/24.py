class MONAD:
    def __init__(self):
        self.var = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def inp(self, var, val):
        self.var[var] = val

    def add(self, a, b):
        if b in self.var:
            self.var[a] += self.var[b]
        else:
            self.var[a] += int(b)

    def mul(self, a, b):
        if b in self.var:
            self.var[a] *= self.var[b]
        else:
            self.var[a] *= int(b)

    def div(self, a, b):
        if b in self.var:
            self.var[a] = self.var[a] // self.var[b]
        else:
            self.var[a] = self.var[a] // int(b)

    def mod(self, a, b):
        if b in self.var:
            self.var[a] = self.var[a] % self.var[b]
        else:
            self.var[a] = self.var[a] % int(b)

    def eql(self, a, b):
        if b in self.var:
            if self.var[a] == self.var[b]:
                self.var[a] = 1
            else:
                self.var[a] = 0
        else:
            if self.var[a] == int(b):
                self.var[a] = 1
            else:
                self.var[a] = 0

    def reset(self):
        self.var = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def process(self, data, num):
        pos = 0
        for line in data:
            if line[0] == 'inp':
                self.inp(line[1], int(num[pos]))
                pos += 1
            if line[0] == 'mul':
                self.mul(line[1], line[2])
            if line[0] == 'add':
                self.add(line[1], line[2])
            if line[0] == 'mod':
                self.mod(line[1], line[2])
            if line[0] == 'div':
                self.div(line[1], line[2])
            if line[0] == 'eql':
                self.eql(line[1], line[2])
        if self.var['z'] == 0:
            print(num)
            return True
        else:
            self.reset()
            return False


def part1(data):
    lines = data.split('\n')
    lines = [line.split(' ') for line in lines]
    num = int('9'*14)
    machine = MONAD()
    while machine.process(lines, str(num)) == False:
        num -= 1
        while '0' in str(num):
            num -= 1


def part2(data):
    pass


if __name__ == "__main__":
    import runner
    runner.run(day=24)
