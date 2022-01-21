import re
from functools import partial
from timeit import timeit


def create_phone_number(n):
    n = "".join(map(str, n))
    return f"({n[0:3]}) {n[3:6]}-{n[6:]}"


def create_phone_number1(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number2(n):
    n = "".join(map(str, n))
    return "(%s) %s-%s" % (n[:3], n[3:6], n[6:])


def create_phone_number3(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)


def create_phone_number4(n):
    n_string = "".join(map(str, n))
    formatted_number = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", n_string)
    return formatted_number


class Test:
    @staticmethod
    def assert_equals(text, result):
        print(text)
        print(text == result)
        search_functions = (
            create_phone_number,
            create_phone_number1,
            create_phone_number2,
            create_phone_number3,
            create_phone_number4,
        )
        n = 10000
        for f in search_functions:
            func_time = timeit(partial(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), number=n)
            print(f"{f.__name__} -- {func_time}")


test = Test
test.assert_equals(
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
)
test.assert_equals(
    create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111"
)
test.assert_equals(
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
)
test.assert_equals(
    create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890"
)
test.assert_equals(
    create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000"
)
