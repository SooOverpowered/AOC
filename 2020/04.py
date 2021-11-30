def byr(a):
    if len(a) == 4:
        if 1920 <= int(a) <= 2002:
            return True
    return False


def iyr(a):
    if len(a) == 4:
        if 2010 <= int(a) <= 2020:
            return True
    return False


def eyr(a):
    if len(a) == 4:
        if 2020 <= int(a) <= 2030:
            return True
    return False


def hgt(a):
    if a.endswith(('cm', 'in')):
        if a.endswith('cm'):
            if 150 <= int(a[:-2:]) <= 193:
                return True
        else:
            if 59 <= int(a[:-2:]) <= 76:
                return True
    return False


def hcl(a):
    if a.startswith('#'):
        string_check = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in range(1, 7):
            if a[i] in string_check or a[i].isdigit():
                pass
            else:
                return False
        return True
    return False


def ecl(a):
    if a in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def pid(a):
    if len(a) == 9:
        for letter in a:
            if letter.isdigit():
                pass
            else:
                return False
        return True
    return False


def part1(data):
    lines=data.rstrip().split('\n')
    processed = ['']
    for line in lines:
        if line != '':
            processed[-1] += ' '+line
        else:
            processed.append('')
    processed = [item.split() for item in processed]
    count = 0
    for passport in processed:
        check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for field in passport:
            if field.startswith('cid'):
                pass
            elif field[0:3] in check:
                check.remove(field[0:3])
        if len(check) == 0:
            count += 1
    return count


Switcher = {'byr': byr, 'iyr': iyr, 'eyr': eyr,
            'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid}


def part2(data):
    lines=data.rstrip().split('\n')
    processed = ['']
    for line in lines:
        if line != '':
            processed[-1] += ' '+line
        else:
            processed.append('')
    processed = [item.split() for item in processed]
    count = 0
    for passport in processed:
        check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for field in passport:
            if field.startswith('cid'):
                pass
            elif field[0:3] in check:
                if Switcher.get(field[0:3])(field[4:]):
                    check.remove(field[0:3])
        if len(check) == 0:
            count += 1
    return count