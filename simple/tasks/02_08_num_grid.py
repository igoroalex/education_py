from typing import List


def num_grid(field: List[List[str]]) -> List[List[str]]:

    for n, row in enumerate(field):
        for m, cell in enumerate(row):
            if cell == "#":
                continue
            field[n][m] = str(
                sum(
                    [
                        1
                        if (len(field) - 1) >= x >= 0
                        and (len(row) - 1) >= y >= 0
                        and field[x][y] == "#"
                        else 0
                        for x in range(n - 1, n + 1 + 1)
                        for y in range(m - 1, m + 1 + 1)
                    ]
                )
            )
    return field


assert num_grid(
    [
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ]
) == [
    ["0", "0", "0", "0", "0"],
    ["0", "1", "1", "1", "0"],
    ["0", "1", "#", "1", "0"],
    ["0", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0"],
]

assert num_grid(
    [
        ["-", "-", "-", "-", "#"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["#", "-", "-", "-", "-"],
    ]
) == [
    ["0", "0", "0", "1", "#"],
    ["0", "1", "1", "2", "1"],
    ["0", "1", "#", "1", "0"],
    ["1", "2", "1", "1", "0"],
    ["#", "1", "0", "0", "0"],
]

assert num_grid(
    [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
    ]
) == [
    ["1", "1", "2", "#", "#"],
    ["1", "#", "3", "3", "2"],
    ["2", "4", "#", "2", "0"],
    ["1", "#", "#", "2", "0"],
    ["1", "2", "2", "1", "0"],
]

print(
    num_grid(
        [
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ]
    )
)

print(
    num_grid(
        [
            ["-", "-", "-", "-", "#"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["#", "-", "-", "-", "-"],
        ]
    )
)

print(
    num_grid(
        [
            ["-", "-", "-", "#", "#"],
            ["-", "#", "-", "-", "-"],
            ["-", "-", "#", "-", "-"],
            ["-", "#", "#", "-", "-"],
            ["-", "-", "-", "-", "-"],
        ]
    )
)
