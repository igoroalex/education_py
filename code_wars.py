from functools import partial
from timeit import timeit
from string import punctuation


def create_phone_number(numbers):
    return numbers


n = 10000


class Test:
    @staticmethod
    def assert_equals(text, result):
        print(text)
        print(text == result)
        search_functions = (
            create_phone_number,
            create_phone_number,
            create_phone_number,
            create_phone_number,
        )
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
