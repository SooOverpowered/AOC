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
            row = prev[y]
            for x in range(width):
                if row[x] == 'L':
                    adjacent = []
                    for temp_row in range(y-1, y+2):
                        if 0 <= temp_row < height:
                            for temp_col in range(x-1, x+2):
                                if 0 <= temp_col < width:
                                    if prev[temp_row][temp_col] == '#':
                                        adjacent.append('#')
                    if len(adjacent) == 0:
                        processed[y][x] = '#'
                elif row[x] == '#':
                    adjacent = []
                    for temp_row in range(y-1, y+2):
                        if 0 <= temp_row < height:
                            for temp_col in range(x-1, x+2):
                                if 0 <= temp_col < width:
                                    if prev[temp_row][temp_col] == '#':
                                        adjacent.append('#')
                    adjacent.remove('#')
                    if len(adjacent) >= 4:
                        processed[y][x] = 'L'
        if processed == prev:
            flag = False
        else:
            prev = [[i for i in row] for row in processed]
    count = 0
    for row in processed:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def count_see(x,y,grid):
    height=len(grid)
    width=len(grid[0])
    count=0
    #north
    for i in range(y-1,-1,-1):
        if grid[i][x]=='L':
            break
        elif grid[i][x]=='#':
            count += 1
            break
    #south
    for i in range(y+1,height):
        if grid[i][x]=='L':
            break
        elif grid[i][x]=='#':
            count += 1
            break
    #east
    for i in range(x+1,width):
        if grid[y][i]=='L':
            break
        elif grid[y][i]=='#':
            count+=1
            break
    #west
    for i in range(x-1,-1,-1):
        if grid[y][i]=='L':
            break
        elif grid[y][i]=='#':
            count+=1
            break
    #north east
    inc=[-1,1]
    while True:
        temp_y=y+inc[0]
        temp_x=x+inc[1]
        if temp_x<0 or temp_x>=width:
            break
        elif temp_y<0 or temp_y>=height:
            break
        elif grid[temp_y][temp_x]=='#':
            count += 1
            break
        elif grid[temp_y][temp_x]=='L':
            break
        else:
            inc[0]-=1
            inc[1]+=1
    #north west
    inc=[-1,-1]
    while True:
        temp_y=y+inc[0]
        temp_x=x+inc[1]
        if temp_x<0 or temp_x>=width:
            break
        elif temp_y<0 or temp_y>=height:
            break
        elif grid[temp_y][temp_x]=='#':
            count += 1
            break
        elif grid[temp_y][temp_x]=='L':
            break
        else:
            inc[0]-=1
            inc[1]-=1
    #south east
    inc=[1,1]
    while True:
        temp_y=y+inc[0]
        temp_x=x+inc[1]
        if temp_x<0 or temp_x>=width:
            break
        elif temp_y<0 or temp_y>=height:
            break
        elif grid[temp_y][temp_x]=='#':
            count += 1
            break
        elif grid[temp_y][temp_x]=='L':
            break
        else:
            inc[0]+=1
            inc[1]+=1
    #southwest
    inc=[1,-1]
    while True:
        temp_y=y+inc[0]
        temp_x=x+inc[1]
        if temp_x<0 or temp_x>=width:
            break
        elif temp_y<0 or temp_y>=height:
            break
        elif grid[temp_y][temp_x]=='#':
            count += 1
            break
        elif grid[temp_y][temp_x]=='L':
            break
        else:
            inc[0]+=1
            inc[1]-=1
    return count
def part2(data):
    lines = data.rstrip().split('\n')
    blocks = [[letter for letter in line] for line in lines]
    prev = [[i for i in row] for row in blocks]
    processed = [[i for i in row] for row in blocks]
    flag = True
    height = len(blocks)
    width = len(blocks[0])
    while flag:
        for y in range(height):
            row = prev[y]
            for x in range(width):
                if row[x] == 'L':
                    if count_see(x,y,prev)==0:
                        processed[y][x] = '#'
                elif row[x] == '#':
                    if count_see(x,y,prev) >= 5:
                        processed[y][x] = 'L'
        if processed == prev:
            flag = False
        else:
            prev = [[i for i in row] for row in processed]
    count = 0
    for row in processed:
        for seat in row:
            if seat == '#':
                count += 1
    return count
