class Factor:
    def __init__(self, factor: int) -> None:
        self.factor = factor

    def is_factor_for(self, candidate):
        return candidate % self.factor == 0


def get_factor_sum(range_max):
    factor_three = Factor(3)
    factor_five = Factor(5)
    factor_sum = 0
    for candidate in range(1, range_max):
        if factor_three.is_factor_for(candidate) or factor_five.is_factor_for(candidate):
            factor_sum += candidate
    return factor_sum


# Factor sum for integers below 10: 23
print("Factor sum for integers below 10: " + str(get_factor_sum(10)))

# Factor sum for integers below 1000: 233168
print("Factor sum for integers below 1000: " + str(get_factor_sum(1000)))

# Factor sum for integers below 1000000: 233333166668
print("Factor sum for integers below 1000000: " + str(get_factor_sum(1000000)))

