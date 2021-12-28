import numpy as np


def convert(data):
    output = [0 if i == '.' else 1 for i in data]
    return output


def transform(ref, img):
    img = np.pad(img, mode='constant', pad_width=1, constant_values=img[0,0])
    output = np.zeros(img.shape, dtype=int)
    for r, row in enumerate(img):
        if 0 < r < len(img)-1:
            for c, cell in enumerate(row):
                if 0 < c < len(row)-1:
                    output[r, c] = ref[int(
                        f'{img[r-1,c-1]}{img[r-1,c]}{img[r-1,c+1]}{img[r,c-1]}{img[r,c]}{img[r,c+1]}{img[r+1,c-1]}{img[r+1,c]}{img[r+1,c+1]}', 2)]
    output = output[1:-1, 1:-1]
    output= np.pad(output, mode='constant', pad_width=1, constant_values=output[0,0])
    return output

def part1(data):
    ref, img = data.split('\n\n')
    ref = convert(ref)
    img = list(map(convert, img.split('\n')))
    img = np.array(img)
    img = np.pad(img, mode='constant', pad_width=2, constant_values=0)
    for i in range(2):
        img = transform(ref, img)
    return np.sum(img)


def part2(data):
    ref, img = data.split('\n\n')
    ref = convert(ref)
    img = list(map(convert, img.split('\n')))
    img = np.array(img)
    img = np.pad(img, mode='constant', pad_width=2, constant_values=0)
    for i in range(50):
        img = transform(ref, img)
    return np.sum(img)


if __name__ == '__main__':
    import runner
    runner.run(day=20)
