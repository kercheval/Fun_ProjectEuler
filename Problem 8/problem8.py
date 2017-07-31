BIG_NUMBER = "73167176531330624919225119674426574742355349194934" + \
    "96983520312774506326239578318016984801869478851843" + \
    "85861560789112949495459501737958331952853208805511" + \
    "12540698747158523863050715693290963295227443043557" + \
    "66896648950445244523161731856403098711121722383113" + \
    "62229893423380308135336276614282806444486645238749" + \
    "30358907296290491560440772390713810515859307960866" + \
    "70172427121883998797908792274921901699720888093776" + \
    "65727333001053367881220235421809751254540594752243" + \
    "52584907711670556013604839586446706324415722155397" + \
    "53697817977846174064955149290862569321978468622482" + \
    "83972241375657056057490261407972968652414535100474" + \
    "82166370484403199890008895243450658541227588666881" + \
    "16427171479924442928230863465674813919123162824586" + \
    "17866458359124566529476545682848912883142607690042" + \
    "24219022671055626321111109370544217506941658960408" + \
    "07198403850962455444362981230987879927244284909188" + \
    "84580156166097919133875499200524063689912560717606" + \
    "05886116467109405077541002256983155200055935729725" + \
    "71636269561882670428252483600823257530420752963450"


def calculate_largest_adjacent_product(num_adjacent):
    current_product = 1
    current_index = 0
    max_index = BIG_NUMBER.__len__() - num_adjacent
    zero_count = 0
    while current_index < num_adjacent and current_index < max_index:
        current_digit = int(BIG_NUMBER[current_index])
        if current_digit == 0:
            zero_count += 1
        else:
            current_product *= current_digit
        current_index += 1

    max_product = current_product
    while current_index < max_index - num_adjacent:
        departing_digit = int(BIG_NUMBER[current_index - num_adjacent])
        current_digit = int(BIG_NUMBER[current_index])

        if departing_digit == 0:
            zero_count -= 1
        else:
            current_product //= departing_digit

        if current_digit == 0:
            if current_digit == 0:
                zero_count += 1
        else:
            current_product *= current_digit

        if zero_count == 0 and current_product > max_product:
            max_product = current_product

        current_index += 1

    return max_product


NUM_ADJACENT = 13

# The largest product of 13 numbers in our 1000 digit number is 23514624000
print("The largest product of " + str(NUM_ADJACENT)
      + " numbers in our 1000 digit number is "
      + str(calculate_largest_adjacent_product(NUM_ADJACENT)))

