# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def generate_dictionary_user_input():

    new_dictionary = {}
    num = int(input("What is your number?: "))

    for i in range(1, num + 1):
        new_dictionary[i] = i*i
    return new_dictionary


def generate_dictionary_param_input(num):

    new_dictionary = {}

    for i in range(1, num + 1):
        new_dictionary[i] = i*i
    return new_dictionary
