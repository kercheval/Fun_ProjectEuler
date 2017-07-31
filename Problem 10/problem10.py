import math

factors = []


def is_prime(number_to_test):
    square_root = math.sqrt(number_to_test)
    for factor in factors:
        if factor > square_root:
            break
        if number_to_test % factor == 0:
            return False
    factors.append(number_to_test)
    return True


def sum_primes(max_prime):
    candidate = 2
    current_sum = 0
    while candidate < max_prime:
        if is_prime(candidate):
            current_sum += candidate
        candidate += 1
    return current_sum


MAX_PRIME = 2000000

# The sum of all primes below 2000000 is 142913828922
print("The sum of all primes below " + str(MAX_PRIME) + " is " + str(sum_primes(MAX_PRIME)))
