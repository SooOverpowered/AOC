def part1(data):
    lines = data.rstrip().split('\n\n')
    rules=lines[0].split('\n')
    messages=lines[1].split('\n')
    rule_dict = {}
    for rule in rules:
        temp = rule.split(': ')
        num = int(temp[0])
        content = temp[1].split(' | ')
        for i, item in enumerate(content):
            anothertemp=item.split(' ')
            anothertemp=[int(i) if i.isnumeric() else i for i in anothertemp]
            content[i]=anothertemp
        rule_dict[num] = content
    rule_dict[77],rule_dict[91]='a','b'
    def check(line, rule):
        if not rule:
            return len(line)==0
        sub_rules = rule_dict[rule.pop(0)]
        if sub_rules in ['a','b']:
            return line.startswith(sub_rules)and check(line[1:],rule)
        else:
            return any(check(line,sub_rule+rule) for sub_rule in sub_rules)
    return sum(check(message,[0]) for message in messages)


def part2(data):
    lines = data.rstrip().split('\n\n')
    rules=lines[0].split('\n')
    messages=lines[1].split('\n')
    rule_dict = {}
    for rule in rules:
        temp = rule.split(': ')
        num = int(temp[0])
        content = temp[1].split(' | ')
        for i, item in enumerate(content):
            anothertemp=item.split(' ')
            anothertemp=[int(i) if i.isnumeric() else i for i in anothertemp]
            content[i]=anothertemp
        rule_dict[num] = content
    rule_dict[8],rule_dict[11]=[[42],[42,8]],[[42,31],[42,11,31]]
    rule_dict[77],rule_dict[91]='a','b'
    def check(line, rule):
        if not rule:
            if len(line)==0:
                return True
            else:
                return False
        lower_rules = rule_dict[rule.pop(0)]
        if lower_rules in ['a','b']:
            return line.startswith(lower_rules)and check(line[1:],rule)
        else:
            return any(check(line,lower_rule+rule) for lower_rule in lower_rules)
    return sum(check(message,[0]) for message in messages)