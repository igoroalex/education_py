# lesson 15
# print("i'm \"beginner\", so what")
# print('c:\\users\\prog1c')
# print(r'c:\users\prog1c')
# print('first string \nsecond\tthird')

a1 = 12
m = f"my name is {a1} and {3.145897:6.2f}"

a2 = 1424
# print(f'{a2=}')

a = 1234578465
# print(f'{a:-^25,}')
# print(f'{a:->25,}')
# print(f'{a:-<25,}')

# плейсхолдеры должны соответствовать типу данных
name = "Odessa"
year = 2021
# print("hello %s %d" % (name, year))

#  формат
string = "{} was started in {}".format(name, year)
# print(string)
string = "{0} was started in {1}".format(name, year)
# print(string)
yw = {"name": "YoungWonks", "year": 2021}
# string = "{name} was started in {year}.".format(name=yw["name"], year=yw["year"])
# print(string)
# https://docs.python.org/3/library/string.html#string-formatting

map1 = ['hello', 'hi', 'privet']
# print(list(map(str.upper, map1)))
# print(list(map(lambda x: x[::-1], map1)))
print(list(map(list, map1)))
