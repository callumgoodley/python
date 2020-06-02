def find_factorial():

    num = int(input("What is the number you want to calculate the factorial of?: "))
    numbers_list = []
    factorial_count = 1

    for i in range(1, num + 1):
        numbers_list.append(i)
    numbers_list.reverse()

    for i in numbers_list:
        factorial_count *= i

    return factorial_count


find_factorial()
