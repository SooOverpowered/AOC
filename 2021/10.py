from statistics import median


def part1(data):
    lines = list(map(list, data.split('\n')))
    brackets = {'<': '>', '[': ']', '{': '}', '(': ')'}
    illegal_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        stack = []
        for bracket in line:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif bracket in brackets.values() and len(stack) > 0:
                if brackets[stack[-1]] == bracket:
                    stack.pop()
                else:
                    score += illegal_score[bracket]
                    break
            else:
                score += illegal_score[bracket]
                break
    return score


def part2(data):
    lines = list(map(list, data.split('\n')))
    brackets = {'<': '>', '[': ']', '{': '}', '(': ')'}
    bracket_score = {')': 1, ']': 2, '}': 3, '>': 4}
    score = []
    for line in lines:
        stack = []
        legal = True
        for bracket in line:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif bracket in brackets.values() and len(stack) > 0:
                if brackets[stack[-1]] == bracket:
                    stack.pop()
                else:
                    legal = False
                    break
            else:
                legal = False
                break
        if legal:
            closing_brackets = [brackets[bracket] for bracket in stack[::-1]]
            temp_score = 0
            for bracket in closing_brackets:
                temp_score *= 5
                temp_score += bracket_score[bracket]
            score.append(temp_score)
    score.sort()
    return median(score)


if __name__ == '__main__':
    import runner
    runner.run(day=10)
