
# Given an integer value and a Boolean value, temperature and isSummer,
# if temperature falls between 60 and 90 (inclusive),
# unless its summer where the upper limit is 100 instead of 90, return True.
# If temperature falls outside this range, return false.


def too_hot(temp, isSummer):
    if temp >= 60 and temp <= 90 and isSummer == False:
        return True
    elif temp >= 60 and temp <= 100 and isSummer == True:
        return True
    else:
        return False


print(too_hot(99, True))
