# lesson24 list
int_list = ['1', '2', '3']
names1 = ['John', 'Bob', 'Alice']
names1[1] = 'Dug'
names1.append('Liam')
names1.pop(1)
names1.sort()
names1.sort(key=len, reverse=True)
names1.reverse()
names1.insert(2, 'Chris')
index_Chris = names1.index('Chris')
count_Chris = names1.count('Chris')
s6 = names1.copy()
# names1.clear()
# print(int_list)
# print(names1)
# sum_lists = sum(int_list, names1)
int_list.extend(names1)
str_list = ', '.join(names1)

q = [['*' for _ in range(5)] for _ in range(5)]
# print(q) # 2d

# сортировка списка словарей по ключу
users = [
    {'name': 'John', 'salary': 200, 'age': 21},
    {'name': 'Danna', 'salary': 400, 'age': 22},
    {'name': 'Yan', 'salary': 500, 'age': 23},
    {'name': 'Abba', 'salary': 100, 'age': 24},
]
u = sorted(users, key=lambda x: (x['salary'], x['age']))
# import operator
# u = sorted(users, key=operator.itemgetter('salary', 'age'))
# print(u)


# dict
codes_cities = [['kiev', 167], ['life', 163], ['vodafone', 150]]
codes_cities1 = dict(codes_cities)
cities = dict.fromkeys(['kiev', 'odessa', 'dhipro'], 100)
code_kiev = codes_cities1.get('kiev')
# объединить словари
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, **y}

codes_cities1.setdefault('mobi', 147)
# print(codes_cities1)
# import json
# print(json.dump(codes_cities, indent=4, sort_keys=True))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
# из двух списков в словарь
new_dict = {k: v for (k, v) in zip(keys, values)}
new_dict1 = dict(zip(keys, values))

mylist = ['a', 'b', 'c']
# из списка в словарь с значением и индексом
new_dict3 = {j: i for (i, j) in enumerate(mylist)}

d = {'Delhi': 121, 'Mumbai': 221, 'New York': 302, 'London': 250}
# убрать знаяения по ключу для нового словаря
new_dict4 = {i: d[i] for i in d.keys() - {'Delhi', 'London'}}

# tuple
my_tuple = (1, 2, 3)
my_typle1 = 1,
my_tuple2 = tuple((1, 2, 3))
# print(my_tuple2.__sizeof__())

s1 = '10 20 30'
x, y, z = map(int, s1.split())
volume = x * y * z

from functools import reduce

volume1 = reduce(
    lambda a, b: a * b,
    map(int, s1.split())
)
# print(volume1)

names = ['Ann', 'Chris', 'Angel', 'Alex']
names_starts_with_a = filter(lambda name: name.startswith('A'), names)
# print(tuple(names_starts_with_a))

# множества set
set1 = {1, 2, 3}
set2 = {3, 4, 5, 1}
# print(set1 & set2)  # пересечение
# print(set1.intersection(set2))  # пересечение
# print(set1 | set2)  # объединение
# print(set1.union(set2))  # объединение
# set1 |= set2
# print(set1)  # объединение
print(set1 - set2)  # вычитание
print(set1 ^ set2)  # объединение без общих
