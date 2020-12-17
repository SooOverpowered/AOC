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
            length=value.bit_length()
            if length==0:
                length=1
            temp = bin(value)
            temp = '0'*(36-length)+temp[2:]
            temp = [letter for letter in temp]
            for i in range(len(mask)):
                if mask[i] == '0':
                    temp[i] = '0'
                elif mask[i] == '1':
                    temp[i] = '1'
            temp = ''.join(temp)
            search_dict[location] = int(temp,2)
    return sum(search_dict.values())


def part2(data):
    pass

print(part1(open('14.txt','r').read()))