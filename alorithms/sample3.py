# def get_cost_of_coffee(number_of_coffees, price_per_coffee):
#     number_of_free_coffees = number_of_coffees // 9
#     number_of_paid = number_of_coffees - number_of_free_coffees
#     return number_of_paid * price_per_coffee


# print(get_cost_of_coffee(7, 2.5))
# print(get_cost_of_coffee(8, 2.5))
# print(get_cost_of_coffee(9, 2.5))
# print(get_cost_of_coffee(19, 2.5))
# print(get_cost_of_coffee(10, 2.5))


import random
import string
import pyperclip

LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SPECIAL = '~!@#$%^&*()_+'

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def generate_password(length):
    if length < 12:
        length = 12

    password = []
    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.append(UPPER_LETTERS[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL[random.randint(0, 12)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 74)])

    random.shuffle(password)
    res = ""
    for chiz in password:
        res += chiz
    pyperclip.copy(res)
    return res


site = input("enter the site name: ")
my_password = generate_password(15)
with open(site+".txt", "w") as my_file:
    my_file.write(my_password)
