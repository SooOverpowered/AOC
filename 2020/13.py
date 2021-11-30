def part1(data):
    lines=data.rstrip().split('\n')
    lines=[int(lines[0]), [int(busid) for busid in lines[1].split(',') if busid != 'x']]
    nearest=None
    current=0
    for busid in lines[1]:
        if nearest==None:
            nearest=busid-lines[0]%busid
            current=busid
        elif lines[0]%busid==0:
            return 0
        else:
            if nearest>busid-lines[0]%busid:
                nearest=busid-lines[0]%busid
                current=busid
    return nearest*current

def part2(data):
    lines= data.rstrip().split('\n')[1].split(',')
    lines=[(i,int(lines[i])) for i in range(len(lines)) if lines[i]!='x']
    jump=lines[0][1]
    time=0
    for item in lines[1:]:
        while (time+item[0])%item[1] != 0:
            time+=jump
        jump*=item[1]
    return time
