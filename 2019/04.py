def process_num(num):
    digit_lst = [int(digit) for digit in str(num)]
    has_repeat_digit = False
    for i in range(5):
        if digit_lst[i] == digit_lst[i+1]:
            has_repeat_digit = True
        if digit_lst[i] > digit_lst[i+1]:
            return False
    if has_repeat_digit:
        return True
    else:
        return False

def process_num_2(num):
    digit_lst = [int(digit) for digit in str(num)]
    digit_count={}
    for i in range(5):
        if digit_lst[i] > digit_lst[i+1]:
            return False
    for digit in digit_lst:
        if digit not in digit_count:
            digit_count[digit]=1
        else:
            digit_count[digit]+=1
    counts=digit_count.values()
    for num in counts:
        if num==2:
            return True
    return False


def part1(data):
    input_range=[int(num) for num in data.rstrip().split('-')]
    num_lst = [i for i in range(input_range[0], input_range[1]+1)]
    count = 0
    for num in num_lst:
        if process_num(num):
            count += 1
    return count

def part2(data):
    input_range=[int(num) for num in data.rstrip().split('-')]
    num_lst = [i for i in range(input_range[0], input_range[1]+1)]
    count = 0
    for num in num_lst:
        if process_num_2(num):
            count += 1
    return count