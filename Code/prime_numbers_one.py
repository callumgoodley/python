# Create an algorithm that determines how many prime numbers are between 1 and 3 million.
# Extension – Have it finish running in under 2 minutes


def find_prime_numbers():

    prime_numbers = []

    for i in range(2, 3000001):
        count = 0
        for j in range(2, i):
            print(i % j)
            if i % j == 0:
                count += 1
        if count == 0:
            prime_numbers.append(i)
    return prime_numbers


find_prime_numbers()
