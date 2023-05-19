# exercise 1:
'''برنامه ای بنویسی که نام و سن کاربر را از ووردی دریافت نماید و در صورتی که
سن او از هشت کمتر بود 
ali is kid
در صورتی که سن ا.و بین هشت و سیزده بود
ali is junior
در صورتی که سن او بین سیزده و هجده بود
ali is teenager
در صورتی که سن او از هجده بزرگتر بود
ali is adult'''

# name = input('Enter your name:> ')
# age = int(input('Enter your age:> '))

# if age < 8:
#     print(f'{name} is kid.')
# elif age >= 8 and age < 13:
#     print(f'{name} is junior.')
# elif age >= 13 and age < 18:
#     print(f'{name} is teenager.')
# else:
#     print(f'{name} is adult.')

# a = 3
# b = 3

# if a == b:
#     print("a and b are equal")
#     print(f"{a} = {b}")
# elif a > b:
#     print("a is greater than b")
#     print(f'{a} > {b}')
# elif a < b :
#     print("a is less than b")
#     print(f'{a} < {b}')

# a = 2
# b = 3
# c = 1

# if a < b and a < c:
#     print(f'{a} is less than {b} and {c}')
# if a < b or a < c:
#     print(f'{a} is less than {b} or {c}')

# exercise : سه عدد از ورودی دریافت کن و بزرگترین و گوچکترین را پرینت


# x = True
# print(not x)
# x = False
# print(not x)

# a = True
# if a:
#     print("something")
# a = False
# if not a:
#     print("something")

# a = True
# b = False

# if a and b:
#     print("something")
# if a or b:
#     print("something else")

# a = 3
# b = 3

# c = a == b
# print(c)

# if 1:
#     print("ok")
# if 0:
#     print("not ok")

# if '':
#     print("blallalla")

user_name = input('Enter the user name:> ')
password = input('enter th password: ')
if user_name == 'admin' and password =="123":
    print("login success")
    print("user is valid")
    print(f"Welcome {user_name}")
else:
    print("login unsuccessful")
    print(f"{user_name} is not valid")
