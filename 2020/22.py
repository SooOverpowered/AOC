def part1(data):
    player1, player2 = data.rstrip().split('\n\n')
    player1 = [int(card) for card in player1.split('\n')[1:]]
    player2 = [int(card) for card in player2.split('\n')[1:]]
    winner = None
    while True:
        one = player1.pop(0)
        two = player2.pop(0)
        if one > two:
            player1.extend([one, two])
        else:
            player2.extend([two, one])
        if len(player1) == 0:
            winner = 2
            break
        elif len(player2) == 0:
            winner = 1
            break
    score = 0
    if winner == 2:
        player2.reverse()
        for i, card in enumerate(player2):
            score += card*(i+1)
    else:
        player1.reverse()
        for i, card in enumerate(player1):
            score += card*(i+1)
    return score


def part2(data):
    player1, player2 = data.rstrip().split('\n\n')
    player1 = [int(card) for card in player1.split('\n')[1:]]
    player2 = [int(card) for card in player2.split('\n')[1:]]
    def play(p1, p2):
        seen = set()
        while p1 and p2:
            round_id = "/".join((":".join(str(x) for x in p1), ":".join(str(x) for x in p2)))
            if round_id in seen:
                return 1, p1
            seen.add(round_id)
            one = p1.pop(0)
            two = p2.pop(0)
            if one <= len(p1) and two <= len(p2):
                if play(p1[:one], p2[:two])[0] == 2:
                    p2.extend([two, one])
                else:
                    p1.extend([one, two])
            else:
                if one > two:
                    p1.extend([one, two])
                else:
                    p2.extend([two, one])
            if len(p1) == 0:
                return 2, p2
            elif len(p2) == 0:
                return 1, p1
    res = play(player1, player2)
    score = 0
    res[1].reverse()
    for i, card in enumerate(res[1]):
        score += card*(i+1)
    return score
