def part1(data, a=[2,5,7,2,10,3,5,6,-1,-5]):
    a.sort()
    return a[-1]

def part2(data, a=[2,5,7,2,10,3,5,6,-1,-5]):
    num=a[0]
    for i in a[1::]:
        if num<i:
            num=i
    return num