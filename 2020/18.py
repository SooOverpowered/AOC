def to_infix(lst):
    queue = []
    ops_stack = []
    while len(lst) != 0:
        temp = lst.pop(0)
        if temp.isnumeric():
            queue.append(temp)
        elif temp in ('+', '*'):
            if len(ops_stack) == 0:
                pass
            elif ops_stack[-1] in ('+', '*'):
                queue.append(ops_stack.pop(-1))
            ops_stack.append(temp)
        elif temp == '(':
            ops_stack.append(temp)
        elif temp == ')':
            while ops_stack[-1] != '(':
                queue.append(ops_stack.pop(-1))
            ops_stack.pop(-1)
    while len(ops_stack) != 0:
        queue.append(ops_stack.pop(-1))
    return queue

def to_infix2(lst):
    queue = []
    ops_stack = []
    while len(lst) != 0:
        temp = lst.pop(0)
        if temp.isnumeric():
            queue.append(temp)
        elif temp in ('+', '*'):
            if len(ops_stack) == 0:
                pass
            elif ops_stack[-1]=='+':
                queue.append(ops_stack.pop(-1))
            ops_stack.append(temp)
        elif temp == '(':
            ops_stack.append(temp)
        elif temp == ')':
            while ops_stack[-1] != '(':
                queue.append(ops_stack.pop(-1))
            ops_stack.pop(-1)
    while len(ops_stack) != 0:
        queue.append(ops_stack.pop(-1))
    return queue

def part1(data):
    lines = data.rstrip().split('\n')
    total=0
    for line in lines:
        line = [string for string in line if string != ' ']
        processed = to_infix(line)
        num=[]
        for token in processed:
            if token.isnumeric():
                num.append(int(token))
            else:
                a=num.pop(-1)
                b=num.pop(-1)
                if token=='+':
                    num.append(a+b)
                elif token=='*':
                    num.append(a*b)
        total+=num[0]
    return total


def part2(data):
    lines = data.rstrip().split('\n')
    total=0
    for line in lines:
        line = [string for string in line if string != ' ']
        processed = to_infix2(line)
        num=[]
        for token in processed:
            if token.isnumeric():
                num.append(int(token))
            else:
                a=num.pop(-1)
                b=num.pop(-1)
                if token=='+':
                    num.append(a+b)
                elif token=='*':
                    num.append(a*b)
        total+=num[0]
    return total



