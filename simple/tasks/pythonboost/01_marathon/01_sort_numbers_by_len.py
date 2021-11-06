def number_len_sort(param: list) -> list:
    return sorted(param, key=lambda x: len(str(x)))


assert number_len_sort([1, 54, 1, 2, 463, 2]) == [1, 1, 2, 2, 54, 463]
assert number_len_sort([999, 421, 22, 990, 32]) == [22, 32, 999, 421, 990]
assert number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]) == [
    9,
    8,
    7,
    6,
    5,
    4,
    2,
    1,
    3,
    31,
]
