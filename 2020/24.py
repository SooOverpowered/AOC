import numpy as np
def part1(data):
    lines = data.rstrip().split('\n')
    tiles = []
    for line in lines:
        temp = [i for i in line]
        processed = []
        while len(temp) != 0:
            if temp[0] == 'n' or temp[0] == 's':
                processed.append(temp[0]+temp[1])
                temp = temp[2::]
            else:
                processed.append(temp.pop(0))
        tiles.append(processed)
    black = []
    for tile in tiles:
        x = 0
        y = 0
        for direction in tile:
            if direction == 'e':
                x += 1
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 'sw':
                y -= 1
            elif direction == 'w':
                x -= 1
            elif direction == 'nw':
                x -= 1
                y += 1
            elif direction == 'ne':
                y += 1
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.append((x, y))
    return len(black)


def part2(data):
    lines = data.rstrip().split('\n')
    tiles = []
    for line in lines:
        temp = [i for i in line]
        processed = []
        while len(temp) != 0:
            if temp[0] == 'n' or temp[0] == 's':
                processed.append(temp[0]+temp[1])
                temp = temp[2::]
            else:
                processed.append(temp.pop(0))
        tiles.append(processed)
    black = []
    for tile in tiles:
        x = 0
        y = 0
        for direction in tile:
            if direction == 'e':
                x += 1
            elif direction == 'se':
                x += 1
                y -= 1
            elif direction == 'sw':
                y -= 1
            elif direction == 'w':
                x -= 1
            elif direction == 'nw':
                x -= 1
                y += 1
            elif direction == 'ne':
                y += 1
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.append((x, y))


print(part2(open('24.txt', 'r').read()))
