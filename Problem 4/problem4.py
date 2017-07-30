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


def get_max_palindromic(number_min, number_max) -> int:
    max_palindromic = number_max  # initial condition
    tuple_1 = number_max
    tuple_2 = number_max
    min_tuple_1 = number_min
    min_tuple_2 = number_min
    while tuple_1 > min_tuple_2 and tuple_1 > min_tuple_1:
        test_product = tuple_1 * tuple_2
        # Mod 11 checks added based on analysis described in solution discussion and reduced runtime by 65%
        if (tuple_1 % 11 == 0 or tuple_2 % 11 == 0) and is_palindromic(test_product):
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


NUMBER_MAX = 999
NUMBER_MIN = 100

# 580085 using 995*583
# 906609 using 993*913
# 886688 using 968*916
# 888888 using 962*924
# 861168 using 932*924
# Max palindromic for 999 is 906609
print("Max palindromic for " + str(NUMBER_MAX) + " is " + str(get_max_palindromic(NUMBER_MIN, NUMBER_MAX)))
