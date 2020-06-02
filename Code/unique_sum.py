
# Given 3 integer values, return their sum. If one value is the same as another value, they do not count towards the sum. Aka only return the sum of unique numbers given.

# Input(1, 2, 3) -> 6
# Input(3, 3, 3) -> 0
# Input(1, 1, 2) -> 2


def unique_sum(num1, num2, num3):

    count = 0

    if num1 != num2 and num1 != num3:
        count += num1
    if num2 != num3 and num2 != num1:
        count += num2
    if num3 != num1:
        count += num3

    return count

