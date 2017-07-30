def is_factor_perfect(candidate, max_factor):
    for factor in range(2, max_factor+1):
        if candidate % factor != 0:
            return False
    return True


def get_smallest_collected_factor(max_factor):
    candidate = max_factor
    while not is_factor_perfect(candidate, max_factor):
        candidate += 2
    return candidate


MAX_FACTOR = 20

# Smallest number factorable by all numbers less then or equal to 20 is  232792560
print("Smallest number factorable by all numbers less then or equal to " + str(MAX_FACTOR) + " is ", str(get_smallest_collected_factor(MAX_FACTOR)))
