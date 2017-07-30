# https://trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm for summation


def sum_of_natural_numbers(max_natural) -> int:
    sum_of_naturals = (max_natural * (max_natural + 1)) // 2
    print("Sum of first n natural numbers for " + str(max_natural) + " is " + str(sum_of_naturals))
    return sum_of_naturals


def square_of_sums_of_natural_numbers(max_natural):
    square_of_sum = sum_of_natural_numbers(MAX_NATURAL) ** 2
    print("Square of sum of first n natural numbers for " + str(max_natural) + " is " + str(square_of_sum))
    return square_of_sum


def sum_of_squares_of_natural_numbers(max_natural):
    sum_of_squares = 0
    for natural in range(1, max_natural+1):
        sum_of_squares += natural ** 2
    print("Sum of squares of first n natural numbers for " + str(max_natural) + " is " + str(sum_of_squares))
    return sum_of_squares


MAX_NATURAL = 100

# Sum of first n natural numbers for 100 is 5050
# Square of sum of first n natural numbers for 100 is 25502500
# Sum of squares of first n natural numbers for 100 is 338350
# Sum squares difference for first n natural numbers for 100 is 25164150
print("Sum squares difference for first n natural numbers for " + str(MAX_NATURAL) + " is " + str(square_of_sums_of_natural_numbers(MAX_NATURAL) - sum_of_squares_of_natural_numbers(MAX_NATURAL)))


