# numbers = [3, 7, 10, 4, 1, 6, 9, 2, 8]


# def median(all_numbers):
#     all_numbers.sort()
#     middle_index = len(all_numbers)//2
#     if len(all_numbers) % 2 == 0:
#         return (all_numbers[middle_index] + all_numbers[middle_index-1])/2
#     return numbers[middle_index]


# print(median(numbers))
names = ["ali", "reza", "artin", "nikan", "nikan"]


numbers = [1, 1, 2, 3, 4]


def my_mode(all_numbers):
    number_count = {}
    count = 0
    max_value = None
    for number in all_numbers:
        if number not in number_count:
            number_count[number] = 0
        number_count[number] += 1
        if number_count[number] > count:
            count = number_count[number]
            max_value = number

    return max_value


print(my_mode(names))
print(my_mode(numbers))
