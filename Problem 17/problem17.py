from num2words import num2words


def count_chars(number_str: str) -> int:
    count = 0
    for char in number_str:
        if char != ' ' and char != '-':
            count += 1
    return count


def total_count_for_numbers(max_number: int) -> int:
    count = 0
    for value in range(1, max_number + 1):
        count += count_chars(num2words(value))
    return count

# TEST = 1
# number_as_string = num2words(TEST)
# print(str(TEST) + " is represented as '" + number_as_string + "' and is "
#       + str(count_chars(number_as_string)) + " characters long")

# Number of characters used to show all numbers from 1 to 1000 is 21124
MAX_NUMBER = 1000
print("Number of characters used to show all numbers from 1 to " + str(MAX_NUMBER) + " is " + str(total_count_for_numbers(MAX_NUMBER)))
