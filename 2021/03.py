gamma = []
epsilon = []


def part1(data):
    lines = data.split('\n')
    global gamma, epsilon
    size = len(lines)
    length = len(lines[0])
    for i in range(length):
        total = sum([int(line[i]) for line in lines])
        if total >= size/2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    temp_gamma = int(''.join(gamma), 2)
    temp_epsilon = int(''.join(epsilon), 2)
    return temp_gamma*temp_epsilon


def part2(data):
    lines = oxygen = co2 = data.split('\n')
    length = len(lines[0])
    for i in range(length):
        if len(oxygen) > 1:
            total_oxygen = sum([int(line[i]) for line in oxygen])
            if total_oxygen >= len(oxygen)/2:
                oxygen = [line for line in oxygen if line[i] == '1']
            else:
                oxygen = [line for line in oxygen if line[i] == '0']
        if len(co2) > 1:
            total_co2 = sum([int(line[i]) for line in co2])
            if total_co2 >= len(co2)/2:
                co2 = [line for line in co2 if line[i] == '0']
            else:
                co2 = [line for line in co2 if line[i] == '1']
    return int(oxygen[0], 2)*int(co2[0], 2)
