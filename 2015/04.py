from hashlib import md5


def part1(data):
    secret = data.rstrip()
    found = False
    number = 1
    while not found:
        password = secret+str(number)
        if md5(password.encode()).hexdigest().startswith('00000'):
            found = True
            return number
        number += 1


def part2(data):
    secret = data.rstrip()
    found = False
    number = 1
    while not found:
        password = secret+str(number)
        if md5(password.encode()).hexdigest().startswith('000000'):
            found = True
            return number
        number += 1
