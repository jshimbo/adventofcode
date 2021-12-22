class Dice:
    def __init__(self):
        self.nextroll = 1
        self.numrolls = 0

    def roll(self):
        total = 0
        for _ in range(3):
            total += self.nextroll
            if self.nextroll == 100:
                self.nextroll = 1
            else:
                self.nextroll += 1
        self.numrolls += 3
        return total


def main():
    dice = Dice()

    winner = False
    positions = {'p1': 4, 'p2': 8}  # practice
    positions = {'p1': 4, 'p2': 7}  # part 1
    scores = {'p1': 0, 'p2': 0}

    players = ['p1', 'p2']
    p_index = 0
    num_players = 2

    booby_score = 0  # score of loser

    while booby_score == 0:
        player = players[p_index]

        roll = dice.roll()

        pos = positions[player]
        pos += roll
        while pos > 10:
            pos -= 10

        positions[player] = pos
        scores[player] += pos

        # print(player, "rolls", roll, "moves to space",
        #       positions[player], "score", scores[player])

        if scores[player] >= 1000:
            # change index to loser
            if p_index == 0:
                player = players[1]
            else:
                player = players[0]

            booby_score = scores[player] * dice.numrolls
            print("log: player, score, numrolls",
                  player, scores[player], dice.numrolls)

        if p_index == (num_players - 1):
            p_index = 0
        else:
            p_index += 1

    print("Loser is", player, "score", booby_score)


if __name__ == '__main__':
    main()
