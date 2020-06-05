def how_many_vowels(str_):
    count = 0
    for letter in str_:
        if ord(letter.upper()) == 65 or ord(letter.upper()) == 69 or ord(letter.upper()) == 73 or ord(letter.upper()) == 79 or ord(letter.upper()) == 85:
            count += 1

    return count


how_many_vowels("Hello World!!!")
