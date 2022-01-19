from functools import partial
from timeit import timeit

__all__ = ["search_needle1"]


def search_needle1(haystack, needle):
    for i in haystack:
        if i == needle:
            return True
    return False


def search_needle2(haystack, needle):
    return needle in haystack


def search_needle3(haystack, needle):
    return any((i == needle for i in haystack))


haystack = list(range(10000))
needle = 9995

n = 10000
search_functions = (search_needle1, search_needle2, search_needle3)
for f in search_functions:
    func_time = timeit(partial(f, haystack, needle), number=n)
    print(f"{f.__name__} -- {func_time}")
