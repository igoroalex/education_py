import math


def pascals_triangle(depth: int):
    for n in range(depth + 1):
        for m in range(n + 1):
            k = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
            print(int(k), end="*")
        print()


pascals_triangle(5)
