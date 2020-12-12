from functools import cache


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

    @cache
    def findbag(name):
        if 'no other bags' in search_dict[name].keys():
            return False
        elif 'shiny gold bags' in search_dict[name].keys():
            return True
        else:
            output = False
            for item in search_dict[name].keys():
                if findbag(item):
                    output = True
                    break
            return output
    for item in search_dict.keys():
        if findbag(item):
            count += 1
    return count


def part2(data):
    lines = data.rstrip('.\n').split('.\n')
    search_dict = {}
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

    @cache
    def searchbag(name):
        if 'no other bags' in search_dict[name].keys():
            return 1
        else:
            return sum([num*searchbag(bag) for bag, num in search_dict[name].items()])+1
    return searchbag('shiny gold bags')-1
