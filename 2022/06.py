from queue import Queue

def parse_signal(data, length):
    q = Queue(4)
    for index, letter in enumerate(data):
        if q.full():
            if len(set(q.queue)) == length:
                return index
            q.get()
        q.put(letter)

def part1(data):
    return parse_signal(data, 4)

    

def part2(data):
    return parse_signal(data, 14)
