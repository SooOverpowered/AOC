def process_num(num):
    digit_lst = [int(digit) for digit in str(num)]
    has_repeat_digit = False
    increasing = True
    for i in range(5):
        if digit_lst[i] == digit_lst[i+1]:
            has_repeat_digit = True
        if digit_lst[i] > digit_lst[i+1]:
            increasing = False
    if has_repeat_digit and increasing:
        return True
    else:
        return False

def process_num_2(num):
    digit_lst = [int(digit) for digit in str(num)]
    has_repeat_digit = False
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


def day4_1():
    num_lst = [i for i in range(158126, 624575)]
    count = 0
    for num in num_lst:
        if process_num(num):
            count += 1
    print(count)

def day4_2():
    num_lst = [i for i in range(158126, 624575)]
    count = 0
    for num in num_lst:
        if process_num_2(num):
            count += 1
    print(count)

day4_2()
