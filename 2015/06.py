def part1(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' through ') for line in lines]
    grid = [[0 for i in range(1000)] for i in range(1000)]
    for i in range(len(lines)):
        if lines[i][0].startswith('toggle'):
            instr = lines[i][0][:6]
            start = lines[i][0][7:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
        elif lines[i][0].startswith('turn on'):
            instr = lines[i][0][:7]
            start = lines[i][0][8:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
        else:
            instr = lines[i][0][:8]
            start = lines[i][0][9:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
    for line in lines:
        if line[0]=='toggle':
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                    if grid[i][j]==0:
                        grid[i][j]=1
                    else:
                        grid[i][j]=0
        elif line[0]=='turn on':
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                    if grid[i][j]==0:
                        grid[i][j]=1
        else:
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                    if grid[i][j]==1:
                        grid[i][j]=0
    count=0
    for row in grid:
        count+=row.count(1)
    return count

def part2(data):
    lines = data.rstrip().split('\n')
    lines = [line.split(' through ') for line in lines]
    grid = [[0 for i in range(1000)] for i in range(1000)]
    for i in range(len(lines)):
        if lines[i][0].startswith('toggle'):
            instr = lines[i][0][:6]
            start = lines[i][0][7:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
        elif lines[i][0].startswith('turn on'):
            instr = lines[i][0][:7]
            start = lines[i][0][8:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
        else:
            instr = lines[i][0][:8]
            start = lines[i][0][9:].split(',')
            end = lines[i][1].split(',')
            lines[i] = [
                instr,
                (int(start[0]), int(start[1])),
                (int(end[0]), int(end[1]))
            ]
    for line in lines:
        if line[0]=='toggle':
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                        grid[i][j]+=2
        elif line[0]=='turn on':
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                        grid[i][j]+=1
        else:
            for i in range(line[1][1],line[2][1]+1):
                for j in range(line[1][0],line[2][0]+1):
                    if grid[i][j]!=0:
                        grid[i][j]-=1
    total=0
    for row in grid:
        total+=sum(row)
    return total
