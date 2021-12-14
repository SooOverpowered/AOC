from re import L


def part1(data):
    lines=data.split('\n')
    count=0
    for line in lines:
        output=line.split(' | ')[1].split(' ')
        for w in output:
            if len(w) in [2,4,3,7]:
                count+=1
    return count

def part2(data):
    lines=data.split('\n')
    total=0
    for line in lines:
        insert, output = line.split(' | ')
        insert=[frozenset(seq) for seq in insert.split(' ')]
        output=[frozenset(seq) for seq in output.split(' ')]
        _1,  _7, _4, *pending, _8 = sorted(set(insert), key=len)
        _6, = [x for x in pending if len(_8 - x) == 1 and len(x & _1) == 1]
        _5, = [x for x in pending if x <= _6 and len(_6 - x) == 1]
        _9, = [x for x in pending if x == _8 - (_6 - _5)]
        _3, = [x for x in pending if len(x - _1) == 3]
        _0, = [x for x in pending if x == (_8 - _4) | _1 | (_8 - _3)]
        _2, = [x for x in pending if len(x - _5) == 2 and len(x & _5) == 3]
        flip = {v: str(i) for i, v in enumerate([_0,_1,_2,_3,_4,_5,_6,_7,_8,_9])}
        total+= int(''.join(flip[x] for x in output))
    return total

if __name__ == "__main__":
    import runner
    runner.run(day=8)