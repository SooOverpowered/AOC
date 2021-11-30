from functools import cache


def part1(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' -> ') for line in lines]
    search_dict = {}
    for line in lines:
        if line[1] not in search_dict.keys():
            search_dict[line[1]] = line[0]
    @cache
    def resolve(item):
        if item.isnumeric():
            return int(item)
        else:
            temp = search_dict[item].split(' ')
            if 'AND' in temp:
                return resolve(temp[0]) & resolve(temp[-1])
            elif 'OR' in temp:
                return resolve(temp[0]) | resolve(temp[-1])
            elif 'NOT' in temp:
                num = resolve(temp[-1])
                binary = bin(num)
                length = num.bit_length()
                binary = '0'*(16-length)+binary[2:]
                binary = ''.join(
                    ['1' if num == '0' else '0' for num in binary])
                return int(binary, 2)
            elif 'LSHIFT' in temp:
                return resolve(temp[0]) << int(temp[-1])
            elif 'RSHIFT' in temp:
                return resolve(temp[0],) >> int(temp[-1])
            else:
                if temp[0].isnumeric():
                    return int(temp[0])
                else:
                    return resolve(temp[0])
    return resolve('a')

def part2(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' -> ') for line in lines]
    search_dict = {}
    for line in lines:
        if line[1] not in search_dict.keys():
            search_dict[line[1]] = line[0]
    @cache
    def resolve(item):
        if item.isnumeric():
            return int(item)
        else:
            temp = search_dict[item].split(' ')
            if 'AND' in temp:
                return resolve(temp[0]) & resolve(temp[-1])
            elif 'OR' in temp:
                return resolve(temp[0]) | resolve(temp[-1])
            elif 'NOT' in temp:
                num = resolve(temp[-1])
                binary = bin(num)
                length = num.bit_length()
                binary = '0'*(16-length)+binary[2:]
                binary = ''.join(
                    ['1' if num == '0' else '0' for num in binary])
                return int(binary, 2)
            elif 'LSHIFT' in temp:
                return resolve(temp[0]) << int(temp[-1])
            elif 'RSHIFT' in temp:
                return resolve(temp[0],) >> int(temp[-1])
            else:
                if temp[0].isnumeric():
                    return int(temp[0])
                else:
                    return resolve(temp[0])
    search_dict['b']=str(resolve('a'))
    resolve.cache_clear()
    return resolve('a')