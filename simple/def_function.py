from typing import List, Union, Optional, Any, Literal, Final, Dict, TypedDict

# typing
def raw_calc(a: Optional, b: Any, c: int, mode: Literal[10, 20, 30]) -> int:
    return (a + b + c) * mode


def calc(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def to_int(a_list: List[str]) -> List[int]:
    return [int(a) for a in a_list]

my_pi: Final = 3.14  # константа, нельзя будет менять
d1: Dict[str, int] = {'a': 1, 'b': True}
class WordStat(TypedDict):
    word: str
    count: int
    comment: str
d2: WordStat = {'word': '458', 'count': 457, 'comment': 'woof'}

class House:
    cats: list = None

    def __init__(self):
        self.cats = []


# Классово верная зверюшка
class Critter(object):
    """Virtual pet"""

    total = 0

    @staticmethod #  к этому классу, и если наследование идет то этот класс возвращает. если classmethod - то класс наследник. но тонкая грань
    def status():
        print(f"всего зверюшек {Critter.total}")

    def __init__(self, name="Carl", mood="good"):
        print("Появилась зверюшка")
        self.__name = name
        Critter.total += 1
        self.__mood = mood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("no name")
        else:
            self.__name = new_name
            print(f"new name {self.__name}")

    def talk(self):
        print(self.__mood)
        print(self.name)

    @staticmethod
    def __private_method__():
        print("это закрытый метод")

    def public_method(self):
        print("это ОТКРЫТЫЙ метод")
        self.__private_method__()


# есть понятие абстрактного класса, в всех def raise NotImplementedError("declare def in subclasses")
# нельяз будет создать экземляр класса наследованика без определения def в классе наследованика
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def perimeter(self):
        print('perimeter')
    def draw(self):
        pass



# deadly diamond death - animal, carnivore, mammal, dog. через super().set_health(10) - чтоб 2 раза не запускать def по наследованию
# MRO - method resolution order последовательность обращения к материнским классам

# одничка, класс который не создает новые экземпляры класса, а всегда использует один и тот же экземпляр класса
class SingleExample:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Pickle - сериализация в файл, и для десерилализации нужно __setstate__ из state
import pickle
class Character:
    def __init__(self, health):
        self.health = health

    def __setstate__(self, state):
        self.health = state.get("health", 100)



# JSON, сериализация классов в udemy урок 83


# def function_with_star(a, b, *, x, y, z):
#     """arguments after * must be named"""
#     return 'with star'
# function_with_star(1, 2, x=4, y=5, z=6)


def unzip_arg(x, y, z):
    """распаковка итеробъекта в аргументы
    если надо разделить позиционные аргументы и распаковку то ставить в аргументах , /,"""
    print(x, y, z)


# unzip_arg(*(1, 2, 3))
# unzip_arg(*[1, 2, 3])
# unzip_arg(*{'x': 1, 'y': 2, 'z': 3})
# unzip_arg(**{'x': 1, 'y': 2, 'z': 3})


class HelloWorld:
    """свой итератор"""

    def __init__(self, num_iters):
        self.num_iters = num_iters
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num_iters:
            self.count += 1
            return "Hello world"
        raise StopIteration


for item in HelloWorld(4):
    # print(item)
    pass


def my_generator(word: str):
    """свой генератор"""
    for letter in word:
        yield letter.upper()


# типа case
def invalid_operation(x, y):
    raise Exception("oooops")


def do_math(x, y, operation="+"):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    return operations.get(operation, invalid_operation)(x, y)


import time

# декоратор
# с нуля
def limit_request_0(seconds):
    """использовать аргументы в декораторе"""

    def limit_request_decorator(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(seconds)
            return result
        return wrap
    return limit_request_decorator
# красиво
from functools import wraps

def limit_request_decorator(func):
    @wraps()
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        time.sleep(3)
        return result
    return wrap


# @limit_request(2)
# def do_something():
#     return 'Hello world'


# callable objects
# встроенные функции len, sorted, встроенные методы str.upper, свои функции и с yield, class, экземпляр class с __call__
# lambda


# closure - замыкание
def hello_human(name):
    def inner_func(name):
        print(f"hello {name}")

    return inner_func


hh1 = hello_human("John")
hh2 = hello_human("KJack")


def adder(num1):
    def inner(num2):
        return num1 + num2

    return inner


a2 = adder(2)


# print(a2(5))
def counter():
    count = 1

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def argkwargs(a, b, /, c, *, d, *f):  # / что слева это позицонные, но справа и позиция и по ключу,
                                    # * все что справа ключевые
                                    # *f все остальные передаваемые аргументы

    pass


# r = counter()
# r()

# isinstance(obj, [classes]) проверка принадлежности объекта к классу


# классы которые ТОЛЬКО хранят данные в атрибутах
from dataclasses import dataclass
@dataclass
class Question:
    text: str = ""
    is_true: bool = False
    explanation: str = ""



# OVERLOAD, перешрузка - это одно имя но возвращает разное
from typing import Union, Literal, overload


@overload
def get_num(a1: int, b1: int, mode: Literal[True]) -> int:
    ...

@overload
def get_num(a1: int, b1: int, mode: Literal[False]) -> str:
    ...


def get_num(a1: int, b1: int, mode: bool) -> Union[str, int]:
    c1 = a1 + b1
    return c1 if mode else str(c1)

# ENUM, типа соответствия, или перечисления чтобы сравнивать
from enum import Enum
class StatusGame(Enum):
    WON = 1
    LOST = 2
    IN_PROGRESS = 3
    NOT_Started = 4

if __name__ == "__main__":
    print()
    # assert def('34wqf') == 'Good'
