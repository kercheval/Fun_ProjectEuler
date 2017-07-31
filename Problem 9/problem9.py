def check_triplet(a, b, c):
    is_right_triangle = a**2 + b**2 == c**2
    if is_right_triangle:
        print("Edge lengths matching constraints: [" + str(a) + "," + str(b) + "," + str(c) + "] with product " + str(a * b * c))
        return True
    return False


def iterate_triplet(edge_constraint) -> []:
    c = edge_constraint - 3
    b = edge_constraint - c - 1
    if b >= c:
        b = c - 1
    a = edge_constraint - b - c
    while b < c and c > 2:
        while a < b:
            if check_triplet(a, b, c):
                return True
            a += 1
            b -= 1
        c -= 1
        b = edge_constraint - c - 1
        if b >= c:
            b = c - 1
        a = edge_constraint - b - c
    return False


EDGE_CONSTRAINT = 1000

# Edge lengths matching constraints: [200,375,425] with product 31875000
# Pythagorean triplet found
if iterate_triplet(EDGE_CONSTRAINT):
    print("Pythagorean triplet found")
else:
    print("Pythagorean triplet not found")

