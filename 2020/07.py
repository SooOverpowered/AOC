def findbag(name, dictionary):
    if 'no other bags' in dictionary[name].keys():
        return False
    elif 'shiny gold bags' in dictionary[name].keys():
        return True
    else:
        output = False
        for item in dictionary[name].keys():
            if findbag(item, dictionary):
                output = True
                break
        return output


def searchbag(name, dictionary):
    if 'no other bags' in dictionary[name].keys():
        return 1
    else:
        return sum([num*searchbag(bag, dictionary) for bag, num in dictionary[name].items()])+1


def part1(data):
    lines = data.rstrip('.\n').split('.\n')
    search_dict = {}
    count = 0
    for line in lines:
        temp = line.split(' contain ')
        bags = temp[1].split(', ')
        search_dict[temp[0]] = {}
        for item in bags:
            t = item.split(' ')
            processed = []
            number = 0
            for i in t:
                if i.isdigit() == False:
                    processed.append(i)
                else:
                    number = int(i)
            processed = ' '.join(processed)
            if processed.endswith('s') == False:
                processed += 's'
            search_dict[temp[0]][processed] = number
    for item in search_dict.keys():
        if findbag(item, search_dict):
            count += 1
    return count


def part2(data):
    lines = data.rstrip('.\n').split('.\n')
    search_dict = {}
    count = 0
    for line in lines:
        temp = line.split(' contain ')
        bags = temp[1].split(', ')
        search_dict[temp[0]] = {}
        for item in bags:
            t = item.split(' ')
            processed = []
            number = 0
            for i in t:
                if i.isdigit() == False:
                    processed.append(i)
                else:
                    number = int(i)
            processed = ' '.join(processed)
            if processed.endswith('s') == False:
                processed += 's'
            search_dict[temp[0]][processed] = number
    return searchbag('shiny gold bags',search_dict)-1
