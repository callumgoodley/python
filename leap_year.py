
# Given a year work out if it is a leap year or not.
# Rule: A year is a leap year if it is divisible by 4, and either divisible by 400 or not divisible by 100.


def leap_year(year):
    if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
        return True
    else:
        return False


print(leap_year(1900))
