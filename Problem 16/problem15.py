def power_of(base: int, exponent: int) -> str:
    current_value = str(base)
    current_exponent = 1
    while current_exponent < exponent:
        new_sum = ""
        beginning = - current_value.__len__()
        digit_index = -1
        remainder = 0
        while digit_index >= beginning:
            count = remainder
            count += int(current_value[digit_index]) << 1
            remainder = count // 10
            new_sum = str(count % 10) + new_sum
            digit_index -= 1
        if remainder > 0:
            new_sum = str(remainder) + new_sum
        current_value = new_sum
        current_exponent += 1
    print("The value " + str(base) + " raised to the power " + str(exponent) + " is " + str(current_value))
    return current_value


def sum_digits(number_str: str) -> int:
    sum = 0
    for digit in number_str:
        sum += int(digit)
    return sum


BASE = 2
EXPONENT = 1000

# The value 2 raised to the power 1000 is 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# The sum of all digits of 2 raised to the power 1000 is 1366
print("The sum of all digits of " + str(BASE) + " raised to the power "
      + str(EXPONENT) + " is " + str(sum_digits(power_of(BASE, EXPONENT))))
