import random
import string
from typing import List
from time import time
from functools import wraps


def add_new_alphabet(alphabet_name, password_alphabet, alphabet_to_add):
    print_message = f"Would you like to add {alphabet_name} to your password('y' if you mean yes/'n' if no)?"
    add_alphabet = input(print_message)
    while True:
        if add_alphabet.lower() == 'y':
            password_alphabet += alphabet_to_add
            break
        elif add_alphabet.lower() == 'n':
            break
        else:
            print('Enter the correct symbol ("y" for yes or "n" for no): ')
            add_alphabet = input(print_message)
    return password_alphabet

def generate_password():
    print("Let's create a strong password for you.")
    password_lenght = input('Choose the length of password (from 4 to 16 symbols): ')
    while True:
        if password_lenght.isalpha():
            print('You typed text, please choose the number from 4 to 16')
            password_lenght = input('Choose the length of password (from 4 to 16 symbols): ')
        elif 4 <= int(password_lenght) <= 16:
            password_lenght = int(password_lenght)
            break
        else:
            print('Choose the correct number')
            password_lenght = input('Choose the length of password(from 4 to 16 symbols): ')
    alphabet_names = ('lowercase', 'uppercase', 'numbers', 'symbols')
    alphabets_to_add = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
    password_alphabet = ''
    for alphabet_name, alphabet_to_add in zip(alphabet_names, alphabets_to_add):
        password_alphabet = add_new_alphabet(alphabet_name=alphabet_name,
                                             alphabet_to_add=alphabet_to_add,
                                             password_alphabet=password_alphabet)
    symbols_list: List = random.choices(password_alphabet, k=password_lenght)
    password = ''.join(symbols_list)
    return password


def time_function(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print(f.__name__ + " " + "took" + " " + str((end - start) * 1000) + 'ms')
        return result
    return wrapper


@time_function
def break_the_password(password):
    for length in range(4, 8):
        for number in range(length):
            test_password = str(number).zfill(length)
            if test_password == password:
                return test_password





if __name__ == '__main__':
    #
    # password = generate_password()
    # print(password)
    answer = break_the_password(generate_password())
    print(answer)
