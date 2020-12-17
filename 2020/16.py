def part1(data):
    lines= data.rstrip().split('\n\n')
    fields=lines[0].split('\n')
    myticket=lines[1].split('\n')[1].split(',')
    nearby=lines[2].split('\n')[1:]
    fields=[line.split(': ') for line in fields]
    fields=[[field[0], field[1].split(' or ')[0], field[1].split(' or ')[1]] for field in fields]
    lst=[]
    for ticket in nearby:
        ticket=ticket.split(',')
        ticket=[int(num) for num in ticket]
        for num in ticket:
            if num<27 or num>974:
                lst.append(num)
    return sum(lst)

def part2(data):
    lines= data.rstrip().split('\n\n')
    fields=lines[0].split('\n')
    myticket=lines[1].split('\n')[1].split(',')
    myticket=[int(num) for num in myticket]
    nearby=lines[2].split('\n')[1:]
    fields=[line.split(': ') for line in fields]
    fields=[[field[0], field[1].split(' or ')[0], field[1].split(' or ')[1]] for field in fields]
    valid=[]
    for ticket in nearby:
        ticket=ticket.split(',')
        ticket=[int(num) for num in ticket]
        flag=True
        for num in ticket:
            if num<27 or num>974:
                flag=False
                break
        if flag:
            valid.append(ticket)
    processed=[]
    for i in range(len(valid[0])):
        temp=[]
        for ticket in valid:
            temp.append(ticket[i])
        processed.append(set(temp))
    field_sets=[]
    for field in fields:
        first=(int(field[1].split('-')[0]),int(field[1].split('-')[1]))
        second=(int(field[2].split('-')[0]),int(field[2].split('-')[1]))
        temp=set(range(first[0],first[1]+1))
        temp.update(range(second[0],second[1]+1))
        field_sets.append([field[0],temp])
    classify=[]
    for i in range(len(processed)):
        temp=set()
        for field in field_sets:
            if processed[i].issubset(field[1]):
                temp.add(field[0])
        classify.append([i,temp])
    res=[13,18,7,6,12,14]
    prod=1
    for num in res:
        prod*=myticket[num]
    return prod 

#part2(open('16.txt','r').read())