def check_accu(lst):
    queue = []
    accu = 0
    cursor = 0
    while cursor < len(lst):
        queue.append(cursor)
        if lst[cursor][0] == 'jmp':
            cursor += int(lst[cursor][1])
        else:
            if lst[cursor][0] == 'acc':
                accu += int(lst[cursor][1])
            cursor += 1
        if cursor in queue:
            return (accu, False, cursor)
        elif cursor == len(lst):
            return (accu, True, cursor)


def part1(data):
    lines = [line.split(' ') for line in data.rstrip().split('\n')]
    return check_accu(lines)[0]


def part2(data):
    lines = [line.split(' ') for line in data.rstrip().split('\n')]
    cursor = check_accu(lines)[2]
    for i in range(cursor, -1, -1):
        temp = lines.copy()
        if temp[i][0] == 'jmp':
            temp[i] = ['nop', temp[i][1]]
        elif temp[i][0] == 'nop':
            temp[i] = ['jmp', temp[i][1]]
        res = check_accu(temp)
        if res[1] == True:
            return res[0]
