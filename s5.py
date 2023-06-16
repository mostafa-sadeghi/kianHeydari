# for i in range(5):
#     print("one")
#     print("two")

# i = 0
# while i < 5:
#     print("one")
#     print("two")
#     i += 1

# i = 0
# t = 0
# while i < 5:
#     n = int(input('enter a number: '))
#     t += n
#     i += 1

# print(t)


# quit = "n"
# while quit == "n":
#     quit = input("Do you want to quit? ")

# done = False
# while not done:
#     quit = input('Do you want to quit? ')
#     if quit == "y":
#         done = True
#     attack = input("Does your elf attack the dragon? ")
#     if attack == "y":
#         print("Bad choice, you died.")
#         done = True


import random

# my_number = random.randint(1,50)
# print(my_number)
actions = ["rock", "paper"," scissors"]
random_index = random.randrange(len(actions))
print(actions[random_index])


