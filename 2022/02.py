CONVERT = {'A': 'X', 'B': 'Y', 'C': 'Z'}
WIN = {'A': 'Z', 'B': 'X', 'C': 'Y'}
LOSE = {'A': 'Y', 'B': 'Z', 'C': 'X'}
SCORE = {'X': 1, 'Y': 2, 'Z': 3}



def part1(data):
    result = 0
    lines = data.split('\n')
    for line in lines:
        opp, choice = line.split(' ')
        if CONVERT[opp] == choice:
            result += SCORE[choice]+3
        elif WIN[opp] == choice:
            result += SCORE[choice]
        else:
            result += SCORE[choice]+6
    return result


def part2(data):
    result = 0
    lines = data.split('\n')
    for line in lines:
        opp, res = line.split(' ')
        if res == 'X':
          result += SCORE[WIN[opp]]
        elif res =='Y':
          result += SCORE[CONVERT[opp]]+3
        else:
          result+= SCORE[LOSE[opp]]+6
    return result
