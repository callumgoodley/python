# Create an algorithm that determines how many prime numbers are between 1 and 3 million.
# Extension – Have it finish running in under 2 minutes


def is_it_prime(num):

    count = 0

    for j in range(2, num):
        if num % j == 0:
            count += 1
        if count > 0:
            break
    return count


def find_prime_numbers():

    prime_count = 0

    for i in range(2, 10001):

        prime_binary = is_it_prime(i)

        if prime_binary == 0:
            prime_count += 1

    print(prime_count)
    return prime_count


find_prime_numbers()
