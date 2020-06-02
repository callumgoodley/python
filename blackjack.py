# Given 2 integer values greater than 0, return whichever value is closest to 21 without going over 21.
# If they both go over 21 then return 0

# Input(18, 21) -> 21
# Input(20, 18) -> 20
# Input(22, 22) -> 0


def blackjack(hand_one, hand_two):

    if hand_one <= 21 and hand_one > hand_two:
        return hand_one
    elif hand_two <= 21 and hand_two > hand_one:
        return hand_two
    elif hand_one > 21 and hand_two > 21:
        return 0
