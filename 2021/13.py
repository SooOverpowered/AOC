import numpy as np
def part1(data):
    dots, folds = data.split('\n\n')
    dots = dots.split('\n')
    dots= [list(map(int, dot.split(','))) for dot in dots]
    folds = folds.split('\n')
    folds = [fold[11::].split('=') for fold in folds]
    for i,fold in enumerate(folds):
        if fold[0]=='x':
            elligible = [dot for dot in dots if dot[0]>int(fold[1])]
            for dot in elligible:
                temp=[2*int(fold[1])-dot[0],dot[1]]
                if temp not in dots:
                    dots.append(temp)
                dots.remove(dot)
        elif fold[0]=='y':
            elligible = [dot for dot in dots if dot[1]>int(fold[1])]
            for dot in elligible:
                temp=[dot[0],2*int(fold[1])-dot[1]]
                if temp not in dots:
                    dots.append(temp)
                dots.remove(dot)
        if i==0:
            return len(dots)

def process_dots(dots):
    max_x= max(dot[0] for dot in dots)
    max_y= max(dot[1] for dot in dots)
    grid=np.zeros((max_y+1,max_x+1), dtype=int)
    for dot in dots:
        grid[dot[1],dot[0]]=4
    for line in grid:
        print(''.join(map(str,line)))

def part2(data):
    dots, folds = data.split('\n\n')
    dots = dots.split('\n')
    dots= [list(map(int, dot.split(','))) for dot in dots]
    folds = folds.split('\n')
    folds = [fold[11::].split('=') for fold in folds]
    for i,fold in enumerate(folds):
        if fold[0]=='x':
            elligible = [dot for dot in dots if dot[0]>int(fold[1])]
            for dot in elligible:
                temp=[2*int(fold[1])-dot[0],dot[1]]
                if temp not in dots:
                    dots.append(temp)
                dots.remove(dot)
        elif fold[0]=='y':
            elligible = [dot for dot in dots if dot[1]>int(fold[1])]
            for dot in elligible:
                temp=[dot[0],2*int(fold[1])-dot[1]]
                if temp not in dots:
                    dots.append(temp)
                dots.remove(dot)
    process_dots(dots)

if __name__ == '__main__':
    import runner
    runner.run(day=13)