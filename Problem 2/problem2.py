def is_even(candidate):
    return candidate % 2 == 0

STOP_SENTINAL = 4000000  # Do not exceed four million on the fib check

even_sum = 0
this_fib = 1
last_fib = 0

while this_fib < STOP_SENTINAL:
    new_fib = this_fib + last_fib
    last_fib = this_fib
    this_fib = new_fib
    if is_even(this_fib):
        even_sum += this_fib

# Sum of even fibs less than 4000000 is 4613732
print("Sum of even fibs less than " + str(STOP_SENTINAL) + " is " + str(even_sum))
