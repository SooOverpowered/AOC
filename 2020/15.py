def part1(data):
    lines = data.rstrip().split(',')
    lines = [int(num) for num in lines]
    search_dict = {}
    cursor = 0
    for i in lines[:-1]:
        search_dict[i]=cursor
        cursor+=1
    latest=lines[-1]
    while cursor+1!=2020:
        if latest in search_dict.keys():
            temp=latest
            latest=cursor-search_dict[temp]
            search_dict[temp]=cursor
        else:
            search_dict[latest]=cursor
            latest=0
        cursor+=1
    return latest
def part2(data):
    lines = data.rstrip().split(',')
    lines = [int(num) for num in lines]
    search_dict = {}
    cursor = 0
    for i in lines[:-1]:
        search_dict[i]=cursor
        cursor+=1
    latest=lines[-1]
    while cursor+1!=30000000:
        if latest in search_dict.keys():
            temp=latest
            latest=cursor-search_dict[temp]
            search_dict[temp]=cursor
        else:
            search_dict[latest]=cursor
            latest=0
        cursor+=1
    return latest