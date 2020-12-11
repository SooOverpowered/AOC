def part1(data):
    lines = [int(num) for num in data.rstrip().split('\n')]
    lines = sorted(lines)
    lines.append(lines[-1]+3)
    lines.insert(0, 0)
    count = {'1': 0, '3': 0}
    for i in range(len(lines)-1):
        if lines[i]+1 == lines[i+1]:
            count['1'] += 1
        elif lines[i]+3 == lines[i+1]:
            count['3'] += 1
    return count['3']*count['1']


def part2(data):
    lines = [int(num) for num in data.rstrip().split('\n')]
    lines = sorted(lines)
    search_dict={0:1}
    for adapter in lines:
        search_dict[adapter]=0
        for i in range(1,4):
            if adapter-i==0 or adapter-i in lines:
                search_dict[adapter]+=search_dict[adapter-i]
    return search_dict[lines[-1]]
