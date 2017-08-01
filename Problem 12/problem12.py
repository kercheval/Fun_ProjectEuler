from typing import List
import math


def find_factors(number_to_test) -> List[int]:
    factors = list()
    lower_factor = 1
    upper_factor = number_to_test
    while lower_factor < upper_factor:
        if number_to_test % lower_factor == 0:
            upper_factor = number_to_test // lower_factor
            factors.append(lower_factor)
            factors.append(upper_factor)
        lower_factor += 1
    factors.sort()
    return factors


# T(n)=n(n+1)/2
def get_natural_with_factors(num_divisors) -> int:
    triangle_index = num_divisors
    current_number = num_divisors*(num_divisors+1)//2
    while find_factors(current_number).__len__() < num_divisors:
        triangle_index += 1
        current_number += triangle_index
    return current_number


NUM_DIVISORS = 500

# The first triangle number with 500 or more divisors is 76576500
print("The first triangle number with " + str(NUM_DIVISORS)
      + " or more divisors is " + str(get_natural_with_factors(NUM_DIVISORS)))
