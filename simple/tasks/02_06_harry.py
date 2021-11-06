from typing import List


def harry(streets: List[List[int]]) -> int:
    """
    делаем 2d матрицу, где для каждого элемента n, m - это максимальное число из
    числа слева+текущее и числа сверху+текущее, учитывая элементы на индексах 0 в 2d матрице
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]] ->
    [1, 3, 6, 10, 15],
    [7, 14, 22, 31, 41],
    [18, 30, 43, 57, 72]]
    """
    for n, street_n in enumerate(streets):
        for m, house in enumerate(street_n):
            streets[n][m] = max(
                sum((house, 0 if n - 1 < 0 else streets[n - 1][m])),
                sum((house, 0 if m - 1 < 0 else streets[n][m - 1])),
            )
    return -1 if not streets[0] else streets[n][m]


assert harry([[5, 2], [5, 2]]) == 12  # (5+5+2)
assert harry([[5, 2, 3]]) == 10  # (5+2+3)

assert (
    harry([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 72
)  # (1+6+11+12+13+14+15)

assert harry([[]]) == -1
