from collections import Counter, defaultdict

from numpy import common_type


def part1(data):
    template, insertion = data.split('\n\n')
    insertion = insertion.split('\n')
    rules = {line.split(' -> ')[0]: line.split(' -> ')[1]
             for line in insertion}
    pairs = Counter()
    chars = Counter(template)
    for i in range(len(template)-1):
        temp = template[i:i+2]
        if temp in rules:
            pairs[temp] += 1
    for step in range(10):
        temp = Counter()
        for k, v in pairs.items():
            first_pair = k[0]+rules[k]
            second_pair = rules[k]+k[1]
            if first_pair in rules:
                temp[first_pair] += v
            if second_pair in rules:
                temp[second_pair] += v
            chars[rules[k]] += v
            pairs[k] = 0
        pairs.update(temp)
    common=chars.most_common()
    return common[0][1] - common[-1][1]


def part2(data):
    template, insertion = data.split('\n\n')
    insertion = insertion.split('\n')
    rules = {line.split(' -> ')[0]: line.split(' -> ')[1]
             for line in insertion}
    pairs = Counter()
    chars = Counter(template)
    for i in range(len(template)-1):
        temp = template[i:i+2]
        if temp in rules:
            pairs[temp] += 1
    for step in range(40):
        temp = Counter()
        for k, v in pairs.items():
            first_pair = k[0]+rules[k]
            second_pair = rules[k]+k[1]
            if first_pair in rules:
                temp[first_pair] += v
            if second_pair in rules:
                temp[second_pair] += v
            chars[rules[k]] += v
            pairs[k] = 0
        pairs.update(temp)
    common=chars.most_common()
    return common[0][1] - common[-1][1]


if __name__ == '__main__':
    import runner
    runner.run(day=14)
