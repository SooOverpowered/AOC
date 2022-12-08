from copy import deepcopy
crates = {1: [i for i in 'BWN'],
          2: [i for i in 'LZSPTDMB'],
          3: [i for i in 'QHZWR'],
          4: [i for i in 'WDVJZR'],
          5: [i for i in 'SHMB'],
          6: [i for i in 'LGNJHVPB'],
          7: [i for i in 'JQZFHDLS'],
          8: [i for i in 'WSFJGQB'],
          9: [i for i in 'ZWMSCDJ']
          }


def part1(data):
    steps = data.split("\n\n")[1]
    working_crates = deepcopy(crates)
    for step in steps.split('\n'):
        parsed = step.split(' ')
        loops = int(parsed[1])
        start = int(parsed[3])
        stop = int(parsed[5])
        boxes = []
        for i in range(loops):
            boxes += working_crates[start].pop()
        working_crates[stop].extend(boxes)
    return ''.join([i[-1] for i in working_crates.values()])


def part2(data):
    steps = data.split("\n\n")[1]
    working_crates = deepcopy(crates)
    for step in steps.split('\n'):
        parsed = step.split(' ')
        loops = int(parsed[1])
        start = int(parsed[3])
        stop = int(parsed[5])
        boxes = working_crates[start][-loops::]
        working_crates[start] = working_crates[start][:-loops:]
        working_crates[stop].extend(boxes)
    return ''.join([i[-1] for i in working_crates.values()])
