import math


def cars_needed(amount_passengers: int) -> int:
    quantity_cars = math.ceil(amount_passengers / 5)
    return quantity_cars


print(cars_needed(5))
print(cars_needed(11))
print(cars_needed(0))

# assert cars_needed(5) == 1
# assert cars_needed(11) == 3
# assert cars_needed(0) == 0
