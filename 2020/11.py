def part1(data):
    lines = data.rstrip().split('\n')
    blocks = [[letter for letter in line] for line in lines]
    prev = [[i for i in row] for row in blocks]
    processed = [[i for i in row] for row in blocks]
    flag = True
    height = len(blocks)
    width = len(blocks[0])
    while flag:
        for y in range(height):
            row=prev[y]
            for x in range(width):
                if row[x]=='L':
                    adjacent=[]
                    for temp_row in range(y-1,y+2):
                        if 0<=temp_row<height:
                            for temp_col in range(x-1,x+2):
                                if 0<=temp_col<width:
                                    if prev[temp_row][temp_col]=='#':
                                        adjacent.append('#')
                    if len(adjacent)==0:
                        processed[y][x]='#'
                elif row[x]=='#':
                    adjacent=[]
                    for temp_row in range(y-1,y+2):
                        if 0<=temp_row<height:
                            for temp_col in range(x-1,x+2):
                                if 0<=temp_col<width:
                                    if prev[temp_row][temp_col]=='#':
                                        adjacent.append('#')
                    adjacent.remove('#')
                    if len(adjacent)>=4:
                        processed[y][x]='L'
        if processed==prev:
            flag=False
        else:
            prev=[[i for i in row] for row in processed]
    count=0
    for row in processed:
        for seat in row:
            if seat == '#':
                count += 1
    return count


def part2(data):
    pass
