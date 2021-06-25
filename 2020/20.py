from os import stat
import numpy as np


def part1(data):
    blocks = data.rstrip().split('\n\n')
    print(len(blocks))
    block_dict = {}
    for block in blocks:
        block_id = int(block.split('\n')[0][5:-1])
        grid = np.zeros([10, 10]).astype('int16')
        for y, line in enumerate(block.split('\n')[1:]):
            for x, char in enumerate(line):
                state = 0 if char == '.' else 1
                grid[y, x] = state
        block_dict[block_id] = grid
    #print(block_dict)
    count_border={}
    for tile in block_dict.values():
        borders=[tile[0],tile[-1],tile[:,0],tile[:,-1]]
        for border in borders:
            if ''.join(border.astype('str')) in count_border:
                count_border[''.join(border.astype('str'))]+=1
            else:
                count_border[''.join(border.astype('str'))]=1
    print(sum([i for i in count_border.values() if i==2]))

def part2(data):
    pass
