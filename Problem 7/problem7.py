factors = []

def is_prime(number_to_test):
    for factor in factors:
        if number_to_test % factor == 0:
            return False
    factors.append(number_to_test)
    return True


def find_nth_prime(n) -> int:
    primes_found = 0
    candidate = 2
    last_prime = 1
    while primes_found < n:
        if is_prime(candidate):
            last_prime = candidate
            primes_found += 1
        candidate += 1
    return last_prime


N = 10001

# The nth prime for n=10001 is 104743
print("The nth prime for n=" + str(N) + " is " + str(find_nth_prime(N)))
