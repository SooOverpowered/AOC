def part1(data):
    lines = data.rstrip().split('\n')
    processed = []
    search_dict = {}
    for line in lines:
        if line.startswith('mask'):
            processed.append([line, ])
        else:
            processed[-1].append(line)
    for block in processed:
        mask = block[0].split(' = ')[1]
        for command in block[1:]:
            location, value = command.split(
                ' = ')[0], int(command.split(' = ')[1])
            location = int(location[4:-1])
            temp = format(value, '036b')
            temp = [letter for letter in temp]
            for i in range(len(mask)):
                if mask[i] == '0':
                    temp[i] = '0'
                elif mask[i] == '1':
                    temp[i] = '1'
            temp = ''.join(temp)
            search_dict[location] = int(temp, 2)
    return sum(search_dict.values())


def part2(data):
    lines = data.rstrip().split('\n')
    processed = []
    search_dict = {}
    for line in lines:
        if line.startswith('mask'):
            processed.append([line, ])
        else:
            processed[-1].append(line)
    for block in processed:
        mask = block[0].split(' = ')[1]
        for command in block[1:]:
            location, value = command.split(
                ' = ')[0], int(command.split(' = ')[1])
            location = int(location[4:-1])
            temp = format(location, '036b')
            temp = [letter for letter in temp]
            numX = mask.count('X')
            locateX = [i for i in range(len(mask)) if mask[i] == 'X']
            for i in range(0, 2**numX):
                locationtemp = [i for i in temp]
                binary = format(i, f'0{numX}b')
                for j in range(len(mask)):
                    if mask[j] == '1':
                        locationtemp[j] = '1'
                for loc in range(len(locateX)):
                    locationtemp[locateX[loc]] = binary[loc]
                locationtemp = int(''.join(locationtemp), 2)
                search_dict[locationtemp] = value
    return sum(search_dict.values())
