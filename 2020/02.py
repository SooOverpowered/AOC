def part1(data):
    lines = data.rstrip().split('\n')
    lines = [line.split() for line in lines]
    count = 0
    for line in lines:
        req = line[0].split('-')
        letter = line[1].rstrip(':')
        passphrase = line[2]
        processed = [a for a in passphrase if a == letter]
        if int(req[0]) <= len(processed) <= int(req[1]):
            count += 1
    return count


def part2(data):
    lines = data.rstrip().split('\n')
    lines = [line.split() for line in lines]
    count = 0
    for line in lines:
        req = line[0].split('-')
        letter = line[1].rstrip(':')
        passphrase = line[2]
        if passphrase[int(req[0])-1] == letter == passphrase[int(req[1])-1]:
            pass
        elif passphrase[int(req[0])-1] == letter or passphrase[int(req[1])-1] == letter:
            count += 1
    return count