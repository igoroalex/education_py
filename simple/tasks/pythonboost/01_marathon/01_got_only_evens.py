
def get_only_evens_my(evens: list) -> list:

    return [a for a, i in enumerate(evens) if not a % 2 and not i % 2]


def get_only_evens(evens: list) -> list:

    return [a for a in evens[::2] if not a % 2]


# assert get_only_evens([1, 3, 2, 6, 4, 8]) == [2, 4]
# assert get_only_evens([0, 1, 2, 3, 4]) == [0, 2, 4]
# assert get_only_evens([1, 2, 3, 4, 5]) == []

def ends_add_to_10_my(numbers):
    return len([a for a in numbers if int(str(abs(a))[0]) + int(str(a)[-1]) == 10])


def ends_add_to_10(numbers):
    # return lambda n: sum([int(x[0]) + int(x[-1]) == 10 for x in map(lambda z: str(z).replace('-', ''), n)])
    return lambda n: sum([int(x[0]) + int(x[-1]) == 10 for x in map(lambda z: abs(z), numbers)])


print(ends_add_to_10([19, 46, 2098]))
assert ends_add_to_10([19, 46, 2098]) == 3
assert ends_add_to_10([33, 44, -55]) == 1
assert ends_add_to_10([]) == 0
