from itertools import permutations


def part1(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' = ') for line in lines]
    lines = [[line[0].split(' to ')[0], line[0].split(
        ' to ')[1], int(line[1])] for line in lines]
    search_dict = {}
    short = None
    for line in lines:
        if line[0] not in search_dict.keys():
            search_dict[line[0]] = {line[1]: line[-1]}
        else:
            search_dict[line[0]][line[1]] = line[-1]
        if line[1] not in search_dict.keys():
            search_dict[line[1]] = {line[0]: line[-1]}
        else:
            search_dict[line[1]][line[0]] = line[-1]
    for p in permutations(search_dict.keys(), len(search_dict.keys())):
        total = 0
        for i in range(len(search_dict.keys())-1):
            total += search_dict[p[i]][p[i+1]]
        if short == None:
            short = total
        elif short > total:
            short = total
    return short


def part2(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' = ') for line in lines]
    lines = [[line[0].split(' to ')[0], line[0].split(
        ' to ')[1], int(line[1])] for line in lines]
    search_dict = {}
    short = None
    for line in lines:
        if line[0] not in search_dict.keys():
            search_dict[line[0]] = {line[1]: line[-1]}
        else:
            search_dict[line[0]][line[1]] = line[-1]
        if line[1] not in search_dict.keys():
            search_dict[line[1]] = {line[0]: line[-1]}
        else:
            search_dict[line[1]][line[0]] = line[-1]
    for p in permutations(search_dict.keys(), len(search_dict.keys())):
        total = 0
        for i in range(len(search_dict.keys())-1):
            total += search_dict[p[i]][p[i+1]]
        if short == None:
            short = total
        elif short < total:
            short = total
    return short
