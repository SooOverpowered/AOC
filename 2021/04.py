class Board:
    def __init__(self, rows):
        self.rows = [list(map(int, row.split())) for row in rows.split('\n')]
        self.size = len(self.rows)

    @staticmethod
    def rotate_90(board):
        list_tuple= list(zip(*board[::-1]))
        return [list(elem) for elem in list_tuple]

    def check(self):
        for row in self.rows:
            if row == ['X'] * self.size:
                return True
        rotated = self.rotate_90(self.rows)
        for r in rotated:
            if r == ['X'] * self.size:
                return True
        return False

    def score(self):
        total = 0
        for row in self.rows:
            for item in row:
                if item != 'X':
                    total += item
        return total

    def remove_num(self, num):
        for index, row in enumerate(self.rows):
            if num in row:
                self.rows[index] = [x if x != num else 'X' for x in row]

    def visualize(self):
        for row in self.rows:
            print(' '.join(map(str, row)))
        print('\n')


def part1(data):
    lines = data.split('\n\n')
    numbers = list(map(int, lines[0].split(',')))
    boards = [Board(line) for line in lines[1::]]
    for num in numbers:
        for board in boards:
            board.remove_num(num)
            if board.check():
                return board.score()*num


def part2(data):
    lines = data.split('\n\n')
    numbers = list(map(int, lines[0].split(',')))
    boards = [Board(line) for line in lines[1::]]
    for num in numbers:
        index=0
        while index<len(boards):
            board=boards[index]
            board.remove_num(num)
            if board.check():
                if len(boards)==1:
                    return board.score()*num
                boards.pop(index)
            else:
                index+=1
            

