from collections import Counter
def part1(data):
    fishes = Counter(list(map(int, data.split(','))))
    for i in range(80):
        temp = Counter()
        for key, value in fishes.items():
            if key == 0:
                temp[6] += value
                temp[8]+=value
            else:
                temp[key-1] += value
        fishes = temp
    return sum(fishes.values())

def part2(data):
    fishes = Counter(list(map(int, data.split(','))))
    for i in range(256):
        temp = Counter()
        for key, value in fishes.items():
            if key == 0:
                temp[8] += value
                temp[6] += value 
            else:
                temp[key-1] += value
        fishes = temp
    return sum(fishes.values())

if __name__ == '__main__':
    import runner
    runner.run(day=6)