def check_vowels(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in string:
        if letter in vowels.keys():
            vowels[letter] += 1
    if sum(vowels.values()) >= 3:
        return True
    return False


def check_string(string):
    for item in ['ab', 'cd', 'pq', 'xy']:
        if item in string:
            return False
    return True


def check_repeat(string):
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return True
    return False


def part1(data):
    lines = data.rstrip().split('\n')
    count = 0
    for line in lines:
        if check_string(line) and check_vowels(line) and check_repeat(line):
            count += 1
    return count