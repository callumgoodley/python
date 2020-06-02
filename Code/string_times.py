
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.


# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'
# string_times('Hi', 0) → ''

def string_times(str, n):
    new_str = str
    if n > 0:
        for i in range(n - 1):
            new_str += str
    else:
        new_str = ''
    return new_str
