# x = [1, 2]
# print(x)
# print(type(x))
# print(len(x))

# print(x[0])
# print(x[1])

# x[0] = 100
# print(x)
# x.append(300)
# print(x)

# del x[1]
# print(x)

# x.remove(300)
# print(x)

# my_list = [10, 100, 202, 55, 67]
# for item in my_list:
#     print(item)

# my_list = ["Spoon", "fork", "knife"]
my_list = [[2, 3], [4, 3], [6, 7]]

# print(my_list[0][0])
# print(my_list[0][1])
# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         if my_list[i][j] % 2 == 0:
#             total += my_list[i][j]

# print(total)
# count = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         count += 1
# print(count)


# x.append(300)
# del x[1]
# x.remove(300)

# names = []
# # نام پنج دانش اموز را از ورودی بگیر ور به لیست اضافه کن
# for i in range(5):
#     new_name = input("Enter a name:> ")
#     names.append(new_name)

# print(names)

# name_to_delete = input("Enter a name to delete:> ")
# names.remove(name_to_delete)
# print(names)


# TODO  برنامه ایبنویس که پنج عدد از ورودی در یافت نماید و به لیستی اضافه نماید
# سپس مجموع اعداد زوج موجود در لیست را محاسبه و نمایش دهید

# TODO  my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
# با کمک حلقه فور، محموع اعداد لیست بالا را محاسبه کن و سپس نمایش بده

# my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# result = 0
# for number in my_list:
#     result += number * 2

# print(result)

# x = "0123456789"
# print("x[0] =", x[0])
# print("x[1] =", x[1])
# print("x[2] =", x[2])
# x = [0,1,2,3,4,5,6,7,8,9]
# print("x[0] =", x[0])
# print("x[1] =", x[1])
# print("x[2] =", x[2])

# print(x[:3])
# print(x[:6])
# print(x[6:9])
# print(x[6:])

# x = "0123456789"
# print(len(x))


# x = [0,1,2,3,4,5,6,7,8,9]
# print(len(x))

months = "JanFebAprMayJunJulAugSepOctNovDec"
print(months[:3])
print(months[3:6])
print(months[6:9])
months_list = []
for i in range(len(months)//3):
    months_list.append(months[i*3:(i+1)*3])

print(months_list)

# TODO  با استفاده از لیست بالا برنامه ای بنویس که شماره ماه را از ورودی دریافت نماید 
# و سپس نام ماه را نمایش دهد