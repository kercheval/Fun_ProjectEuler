def is_palindromic(candidate: int):
    check_string = str(candidate)
    first_index = 0
    last_index = -1
    while first_index < check_string.__len__():
        if check_string[first_index] != check_string[last_index]:
            return False
        first_index += 1
        last_index -= 1
    return True


def get_max_palindromic(number_base) -> int:
    max_palindromic = number_base  # initial condition
    tuple_1 = number_base
    tuple_2 = number_base
    min_tuple_2 = 1
    while tuple_1 > min_tuple_2:
        test_product = tuple_1 * tuple_2
        if is_palindromic(test_product):
            print(str(test_product) + " using " + str(tuple_1) + "*" + str(tuple_2))
            if (test_product > max_palindromic):
                max_palindromic = test_product
            min_tuple_2 = tuple_2
            tuple_2 = tuple_1 - 1
            tuple_1 -= 1
        elif tuple_2 <= min_tuple_2:
            tuple_2 = tuple_1 - 1
            tuple_1 -= 1
        else:
            tuple_2 -= 1
    return max_palindromic


NUMBER_BASE = 999

# 90909 using 999*91
# 580085 using 995*583
# 906609 using 993*913
# 886688 using 968*916
# 888888 using 962*924
# 861168 using 932*924
# Max palindromic for 999 is 906609
print("Max palindromic for " + str(NUMBER_BASE) + " is " + str(get_max_palindromic(NUMBER_BASE)))
