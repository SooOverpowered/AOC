def part1(data):
    card, door = data.rstrip().split('\n')
    card = int(card)
    door = int(door)
    card_value = 1
    door_value = 1
    card_loop = 0
    door_loop = 0

    def loop(value, subject):
        value = value*subject
        value = value % 20201227
        return value
    while True:
        card_value = loop(card_value, 7)
        card_loop += 1
        if card_value == card:
            break
    while True:
        door_value = loop(door_value, 7)
        door_loop += 1
        if door_value == door:
            break
    card_value = 1
    door_value = 1
    for i in range(card_loop):
        card_value = loop(card_value, door)
    for j in range(door_loop):
        door_value = loop(door_value, card)
    return card_value


def part2(data):
    pass



