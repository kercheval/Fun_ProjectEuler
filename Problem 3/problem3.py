from typing import List


def find_factors(number_to_test) -> List[int]:
    factors = list()
    lower_factor = 2
    upper_factor = (number_to_test + 1) // 2
    while lower_factor < upper_factor:
        if number_to_test % lower_factor == 0:
            upper_factor = number_to_test // lower_factor
            factors.append(lower_factor)
            factors.append(upper_factor)
        lower_factor += 1
    factors.sort()
    return factors


def is_prime(number_to_test):
    return find_factors(number_to_test).__len__() == 0


def find_largest_prime_factor(number_to_test) -> int:
    ordered_factors = find_factors(number_to_test)
    if ordered_factors.__len__() == 0:
        return number_to_test
    while ordered_factors.__len__() > 0:
        factor = ordered_factors.pop(-1)
        if is_prime(factor):
            return factor

TEST_NUMBER = 600851475143

# The largest prime factor of 600851475143 is 6857
print("The largest prime factor of " + str(TEST_NUMBER) + " is " + str(find_largest_prime_factor(TEST_NUMBER)))
