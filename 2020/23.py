def part1(data):
    line = data.rstrip()
    line = [int(i) for i in line]
    current = 0

    def adjust(pos, item, lst):
        while lst[pos] != item:
            lst.append(lst.pop(0))
        return lst
    for i in range(100):
        current_cup = line[current]
        pickup = []
        for j in range(1, 4):
            if current+j >= len(line):
                pickup.append(line[current+j-len(line)])
            else:
                pickup.append(line[current+j])
        dest = line[current]-1
        for item in pickup:
            line.remove(item)
        while dest not in line:
            dest -= 1
            if dest < min(line):
                dest = max(line)
        dest_index = line.index(dest)+1
        for j in range(3):
            line.insert(dest_index, pickup.pop(-1))
        line = adjust(current, current_cup, line)
        current += 1
        if current == len(line):
            current = 0
    return line


def part2(data):
    line = data.rstrip()
    line = [int(i) for i in line]
    line.extend(range(max(line)+1, 1000001))
    current = 0

    def adjust(pos, item, lst):
        while lst[pos] != item:
            lst.append(lst.pop(0))
        return lst
    for i in range(10000000):
        current_cup = line[current]
        pickup = []
        for j in range(1, 4):
            if current+j >= len(line):
                pickup.append(line[current+j-len(line)])
            else:
                pickup.append(line[current+j])
        dest = line[current]-1
        for item in pickup:
            line.remove(item)
        while dest not in line:
            dest -= 1
            if dest < min(line):
                dest = max(line)
        dest_index = line.index(dest)+1
        for j in range(3):
            line.insert(dest_index, pickup.pop(-1))
        line = adjust(current, current_cup, line)
        current += 1
        if current == len(line):
            current = 0
    cup1 = line.index(1)
    return line[cup1+1]*line[cup1+2]


print(part2(open('23.txt', 'r').read()))
