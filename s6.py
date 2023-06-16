# numbers = []
# for i in range(3):
#     new_number = int(input('enter a number: '))
#     numbers.append(new_number)


# print(numbers)
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])


# numbers = [1,2,3,4,5]

# numbers.remove(3)

# print(numbers)

# del numbers[0]
# print(numbers)


numbers =(1,2,3,4,5)
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")

# numbers[0] =100 # error


# favorite_sports = ["footbal", "tennis","pingpong"]

favorite_sports= {
    'sara':"football",
    "nikan":"voleyball",
    "reza":"tennis"
}

print("nikan likes:",favorite_sports["nikan"])
print("sara likes:",favorite_sports["sara"])

favorite_sports["artin"] = "football"
print(favorite_sports)

del favorite_sports["reza"]

print(favorite_sports)
# برنامه ای بنویسی که نام چند درس  و نمرات آنها را از ورودی بگیرد و در 
# یک دیکشنری ذخیره نماید
# در پایان معدل فرد را محاسبه کند
# معدل میشه جمع نمرات تقسیم بر تعداشان