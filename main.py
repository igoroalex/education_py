from functools import partial
from timeit import timeit
from string import punctuation


def pig_it(s):
    return " ".join(_ if _ in punctuation else f"{_[1:]}{_[0]}ay" for _ in s.split())


class Test:
    @staticmethod
    def assert_equals(text, result):
        print(text)
        print(text == result)


test = Test
test.assert_equals(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
test.assert_equals(pig_it("This is my string"), "hisTay siay ymay tringsay")
test.assert_equals(pig_it("O tempora o mores !"), "Oay emporatay oay oresmay !")


# n = 10000
# search_functions = (solution, solution2, solution3, solution4, solution5)
# for f in search_functions:
#     func_time = timeit(partial(f, "breakCamelCase"), number=n)
#     print(f"{f.__name__} -- {func_time}")
