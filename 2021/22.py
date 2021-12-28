import numpy as np


def process_coords(data):
    coors = list(map(int, data[2::].split('..')))
    return sorted(coors)


def part1(data):
    lines = data.split('\n')[:21]
    reactor = np.zeros([200,200,200], dtype=int)
    offset=100
    for line in lines:
        command, region = line.split(' ')
        x_reg, y_reg, z_reg = list(map(process_coords, region.split(',')))
        if command == 'on':
            reactor[x_reg[0]+offset:x_reg[1]+offset+1, y_reg[0]+offset:y_reg[1]+offset+1, z_reg[0]+offset:z_reg[1]+offset+1] = 1
        else:
            reactor[x_reg[0]+offset:x_reg[1]+offset+1, y_reg[0]+offset:y_reg[1]+offset+1, z_reg[0]+offset:z_reg[1]+offset+1] = 0
    return np.sum(reactor[-50+offset:51+offset, -50+offset:51+offset, -50+offset:51+offset])

def part2(data):
    lines = data.split('\n')[:21]
    offset=100
    points=set()


if __name__ == '__main__':
    import runner
    runner.run(day=22)
