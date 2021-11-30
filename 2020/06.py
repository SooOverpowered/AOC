def part1(data):
    blocks=data.rstrip().split('\n\n')
    blocks=[item.split('\n') for item in blocks]
    output=0
    for block in blocks:
        if len(block)==1:
            output+=len(block[0])
        else:
            block=[set(item) for item in block]
            output+=len(block[0].union(*block))
    return output

def part2(data):
    blocks=data.rstrip().split('\n\n')
    blocks=[item.split('\n') for item in blocks]
    output=0
    for block in blocks:
        if len(block)==1:
            output+=len(block[0])
        else:
            block=[set(item) for item in block]
            output+=len(block[0].intersection(*block))
    return output