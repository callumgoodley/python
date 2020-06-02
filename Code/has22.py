# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):

    store = [0]
    has22 = False

    for i in nums:
        if i == 2 and i == store[0]:
            has22 = True
        store[0] = i
    return has22
