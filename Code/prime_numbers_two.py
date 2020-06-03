# Prime Numbers 2
# Create an algorithm that determines how many prime numbers are between 1 and 2 billion.
# Extension – Have it finish running in under 3 minutes


def is_it_prime(num):
    for j in range(2, num + 1):
        if num % j == 0:
            return 1
        else:
            return 0


def how_many_prime():

    prime_count = 0

    for i in range(2, 2000000001):
        count = 0
        count += is_it_prime(i)
        if count == 0:
            prime_count += 1
    print(prime_count)
    return prime_count


how_many_prime()
