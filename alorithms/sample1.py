# def get_chess_square_color(row, column):
#     if row % 2 == column %2:
#         return 'White'
#     else:
#         return "black"


# print(get_chess_square_color(1,1))
# print(get_chess_square_color(2,2))
# print(get_chess_square_color(2,5))
# print(get_chess_square_color(5,5))
# print(get_chess_square_color(3,6))
# print(get_chess_square_color(4,2))


# message = """
# Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
# """


# def count_on_sentences(paragraph):
#     count = 0
#     sentences = []
#     start_index = 0
#     for i in range(len(paragraph)):
#         if paragraph[i] == "." and paragraph[i+1] == " ":
#             count += 1
#             sentences.append(paragraph[start_index:i+1])
#             start_index = i+1
#     return count, sentences


# print(count_on_sentences(message))


# x = '27'
# print(x.isnumeric())

# y = 'B87F'
# print(y.isalnum())


message = """
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
"""

# new_message = message.replace("from", "to")
# print(new_message)

# def findAndReplace(text, oldtext, newtext):
#     replacedText = ''
#     i = 0
#     while i < len(text):
#         if text[i:i+len(oldtext)] == oldtext:
#             replacedText += newtext
#             i += len(oldtext)

#         else:
#             replacedText += text[i]
#             i += 1

#     return replacedText

# print(findAndReplace("python is the best programming language and so i love python", "python", "javascript"))


# def get_hours_minutes_seconds(time):
#     if time >= 3600:
#         hours = time // 3600
#         time = time % 3600
#     else:
#         hours = 0

#     if time >= 60:
#         minutes = time // 60
#         time = time % 60
#     else:
#         minutes = 0

#     seconds = time
#     return f"{hours}h:{minutes}m:{seconds}s"

# print(get_hours_minutes_seconds(30))
# print(get_hours_minutes_seconds(60))
# print(get_hours_minutes_seconds(90))
# print(get_hours_minutes_seconds(3600))
# print(get_hours_minutes_seconds(3610))
# print(get_hours_minutes_seconds(34678))

# numbers = [28,25,42,2]
# print(min(numbers))
# print(max(numbers))


# def min_number(all_numbers):
#     smallest = all_numbers[0]
#     for n in all_numbers:
#         if n < smallest:
#             smallest = n

#     return smallest

# print(min_number(numbers))

# def max_number(all_numbers):
#     largest = all_numbers[0]
#     for n in all_numbers:
#         if n > largest:
#             largest = n

#     return largest

# print(min_number(numbers))
# print(max_number(numbers))

numbers = [2, 4, 6, 8]
# TODO  define a function that calculate the sum of all numbers in the list (calculate_sum)
# TODO define a function that multiplies all numbers in the list (calculateMul)

print("sum is: ",sum(numbers))

def my_sum(all_numbers):
    total = 0
    for num in all_numbers:
        total += num
    return total
print("sum is: ",my_sum(numbers))


# def average(all_numbers):
#     return sum(all_numbers)/len(all_numbers)


# def average(all_numbers):
#     total = 0
#     count = 0
#     for number in all_numbers:
#         total += number
#         count += 1
#     return total/count


# print(average(numbers))
