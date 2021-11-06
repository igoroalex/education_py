def sum_digits_number(up_number: int) -> int:
    sum_digits = 0
    while up_number > 0:
        sum_digits += up_number % 10
        up_number //= 10
    return sum_digits


def sum_digits_number1(up_number: int) -> int:
    return sum([int(i) for i in str(up_number)])


if __name__ == "__main__":
    print(sum_digits_number(100000058))
    print(sum_digits_number1(100000058))
