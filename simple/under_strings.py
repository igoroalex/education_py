
# сортировка списка по ключу словаря
users = [
    {"name": "John", "salary": 200, "age": 21},
    {"name": "Danna", "salary": 400, "age": 22},
    {"name": "Yan", "salary": 500, "age": 23},
    {"name": "Abba", "salary": 100, "age": 24},
]
u = sorted(users, key=lambda _: (_["salary"], _["age"]))
# print(u)

from itertools import product

# это как-бы три вложенных цикла
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]
for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        pass
# print(a, b, c)
# работа с циклами и itertools https://pythonist.ru/czikl-for-v-python-tonkosti-napisaniya/?utm_source=telegram&utm_medium=pythonist

# транспонирование матрицы
m = [[2, 1, 3], [4, 5, 6]]
trans_m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
trans_m_zip = [list(row) for row in zip(*m)]
# print(trans_m)

# zip and unzip
q = [10, 20, 30, 40]
w = [123, 234, 345, 456]
e = "absd"
zip1 = zip(q, w, e)
col1, col2, col3 = zip(*zip1)
# print(col1, col2, col3)


# counter как словарь, можно обращаться к несуществующему ключу
from collections import Counter
import collections

def most_letters():
    # collections.Counter позволяет находить
    #       наиболее часто встречающиеся элементы
    # в итерируемом объекте:
    letter_counter = collections.Counter("Hello world")
    print(letter_counter)
    c = letter_counter.most_common(3)
    print(c)

s1 = "abracadabra"
# items, keys, values, но есть и elements (сстолько раз сколько каунтеров)
let1 = Counter(s1)
let2 = Counter([1, 1, 1, 1, 2, 2, 2, 3])
let3 = Counter()
for i in [1, "a", 1, "a", 2, "b", 2, 3]:
    let3[i] += 1

q2 = let1.most_common(2)  # часто встречающиеся
# print(let3 + let2)
# print(let3 - let2)

# словарь при обращении к несуществующему ключу создает с значением по умолчанию
from collections import defaultdict

r1 = defaultdict(int)
r2 = defaultdict(lambda: [1, 2, 3])
r2.default_factory = lambda: "hello"
r2["d"]
# print(r2)

# работа с итератором с функцией
# for l in iter(input, 'end'):
#     pass
# print(l.upper())
# ints = [_ for _ in iter(input, '')]
# print(ints)

# распечатать из итератора
# [print(_) for _ in range(5)]


# ITERTOOLS - работа с итераторами
import itertools as it

even_numbers = it.count(0, 2)  #  получение четных чисел
# print(list(zip(even_numbers, ['a', 'b', 'c']))) #  [(0, 'a'), (2, 'b'), (4, 'c')]
# [print(_, end=" ") for _ in it.repeat(1, 5)] #  1 1 1 1 1
# letters = it.cycle(['a', 'b', 'c'])
# [
#     print(next(letters), end=" ") for _ in range(10)
# ]  #  a b c a b c a b c a зацикленно, когда доходит до последнего переходит на первый
# print(list(it.chain('abd', 'cef'))) #  ['a', 'b', 'd', 'c', 'e', 'f'] можно объединить списки
# print(list(it.chain.from_iterable(['abd', 'cef']))) #  ['a', 'b', 'd', 'c', 'e', 'f']
# print(list(it.dropwhile(lambda x: x < 3, range(10)))) #  [3, 4, 5, 6, 7, 8, 9] дропает пока верно
# print(list(it.takewhile(lambda x: x < 3, range(10)))) #  [0, 1, 2] берет пока верно
players = ["Alex", "Ann", "Ivan", "Neo"]
ratings = [4, 6, 7]
# print(list(zip(players, ratings)))  # [('Alex', 4), ('Ann', 6), ('Ivan', 7)] by default
# print(dict(zip(players, ratings)))  # {'Alex': 4, 'Ann': 6, 'Ivan': 7} by default
# print(
#     dict(it.zip_longest(players, ratings, fillvalue=10))
# )  # {'Alex': 4, 'Ann': 6, 'Ivan': 7, 'Neo': 10} если разное колво эелментов в списках
# for key, grp in it.groupby([1, 1, 2, 2, 2, 3]):  # но только если последовательно идут значения, более сложное 85 урок
#     print(f"{key=} {list(grp)=}")
# it.permutations([1, 4, 6, 7])  # все комбинации
# print(list(it.combinations('abcd', 2)))  # [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]


