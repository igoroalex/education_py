"""Кодинг-марафон. Задача № 10.
Лабиринт может быть представлен двухмерной матрицей, где нули представляют области, по которым можно ходить,
а единицы - стены. Вы начинаете движение с верхнего левого угла, а выход находится в самой нижней правой ячейке.
Создайте функцию, которая возвращает истину, если вы можете пройти от одного конца лабиринта до другого.
Двигаться можно только вверх, вниз, влево и вправо. По диагонали двигаться нельзя.
Примечания:
1. В лабиринте размером m x n вы входите в [0, 0] и выходите в [m-1, n-1].
2. За эту задачу можно будет получить дополнительные 10 балов (т.е. всего 20), если сделать визуализацию алгоритма
поиска пути при помощи модуля turtle либо его аналогов.
3. Также эту задачу не обязательно сдавать на repl.it - страницы на гитхабе либо просто файла будет достаточно.
"""
import turtle

x0, y0 = -200, 200
dx, dy = 40, 40


def draw_cell(i: int, j: int, step_level: int):
    wall = turtle.Turtle(shape="square")
    wall.speed(0)
    wall.up()
    wall.goto(x0 + j * dx, y0 - i * dy)
    wall.shapesize(2)
    wall.color("brown" if step_level == 1 else "yellow")


def draw_maze(maze: list):
    for n, row in enumerate(maze):
        for m, cell in enumerate(row):
            draw_cell(n, m, maze[n][m])


def draw_step(i: int, j: int):
    wall = turtle.Turtle(shape="circle")
    wall.speed(1)
    wall.up()
    wall.goto(x0 + j * dx, y0 - i * dy)
    wall.shapesize(0.5)


def can_exit(maze: list):
    n, m = len(maze) - 1, len(maze[0]) - 1
    draw_maze(maze)

    def step(i: int, j: int, step_level: int):
        if maze[n][m] > 1:
            return maze
        maze[i][j] = step_level
        draw_step(i, j)
        if j + 1 <= m:
            if maze[i][j + 1] == 0 or (
                maze[i][j + 1] != 1 and maze[i][j + 1] > step_level
            ):
                step(i, j + 1, step_level + 1)
        if i + 1 <= n:
            if maze[i + 1][j] == 0 or (
                maze[i + 1][j] != 1 and maze[i + 1][j] > step_level
            ):
                step(i + 1, j, step_level + 1)
        if i - 1 >= 0:
            if maze[i - 1][j] == 0 or (
                maze[i - 1][j] != 1 and maze[i - 1][j] > step_level
            ):
                step(i - 1, j, step_level + 1)
        if j - 1 >= 0:
            if maze[i][j - 1] == 0 or (
                maze[i][j - 1] != 1 and maze[i][j - 1] > step_level
            ):
                step(i, j - 1, step_level + 1)
        return maze

    route = step(0, 0, 2)

    # for i in range(len(route)):
    #     print(route[i])
    return route[n][m] > 1


# can_exit(
#     [
#         [0, 1, 1, 1, 1, 1, 1],
#         [0, 0, 1, 1, 0, 1, 1],
#         [1, 0, 0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 0, 0, 1],
#         [1, 1, 1, 1, 1, 0, 0],
#     ]
# )
#
# can_exit(
#     [
#         [0, 1, 1, 1, 1, 1, 1],
#         [0, 0, 1, 0, 0, 1, 1],
#         [1, 0, 0, 0, 0, 1, 1],
#         [1, 1, 0, 1, 0, 0, 1],
#         [1, 1, 0, 0, 1, 1, 1],
#     ]
# )
# # В этом лабиринте одни тупики!
#
# can_exit(
#     [
#         [0, 1, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1],
#     ]
# )
# # # Выход так близко, но недостижим!
# #
# can_exit(
#     [
#         [0, 1, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0],
#         [1, 0, 0, 0, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 0],
#     ]
# )


assert (
    can_exit(
        [
            [0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 0],
        ]
    )
    == True
)

assert (
    can_exit(
        [
            [0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 1],
        ]
    )
    == False
)
# В этом лабиринте одни тупики!

assert (
    can_exit(
        [
            [0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1],
        ]
    )
    == False
)
# Выход так близко, но недостижим!

assert (
    can_exit(
        [
            [0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 0],
        ]
    )
    == True
)
