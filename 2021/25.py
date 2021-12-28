def part1(data):
    lines = data.split('\n')
    height = len(lines)
    width = len(lines[0])
    rights = set()
    downs = set()
    right_moved = set((1,1))
    down_moved = set((1,1))
    steps=0
    for l, line in enumerate(lines):
        for r, space in enumerate(line):
            if space == '>':
                rights.add((l, r))
            elif space == 'v':
                downs.add((l, r))
    while sum((len(down_moved), len(right_moved)))!=0:
        temp_rights=set()
        temp_downs=set()
        right_moved, down_moved = set(), set()
        for l, r in rights:
            temp = (l, r+1) if r+1 < width else (l, 0)
            if temp not in downs and temp not in rights:
                temp_rights.add(temp)
                right_moved.add((l,r))
        for moved in right_moved:
            rights.remove(moved)
        rights.update(temp_rights)
            
        for l, r in downs:
            temp = (l+1, r) if l+1 < height else (0, r)
            if temp not in rights and temp not in downs:
                temp_downs.add(temp)
                down_moved.add((l,r))
        for moved in down_moved:
            downs.remove(moved)
        downs.update(temp_downs)
        steps+=1
    return steps

def part2(data):
    pass


if __name__ == '__main__':
    import runner
    runner.run(day=25)
