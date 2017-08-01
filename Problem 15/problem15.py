import math


# x_max+y_max steps choosing a combination of x_max or y_max
def getRouteCount(x_max: int, y_max: int) -> int:
    return math.factorial(x_max + y_max)//(math.factorial(x_max) * math.factorial(y_max))


GRID_MAX = 20
grid_size = 1
while grid_size <= GRID_MAX:
    print("Max routes through grid of size [" + str(grid_size) + "," + str(grid_size)
          + "] is " + str(getRouteCount(grid_size, grid_size)))
    grid_size += 1
