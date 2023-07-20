""" Функции """

name = "value"

# input()
# print()
# max
# pow
# ...

# функция - именованный блок кода/имя, который содержит набор действий. 
# функция может принимать какие-то аргументы, проводить над ними действия и возвращать какой-либо результат

# PEP8


# def print_greeting():
#     """ This function doing something """
#     print('Hello world')


# print_greeting()
# print(print_greeting.__doc__)


# def func(x: int, y: int):
#     print(x + y)


# func(10, 20)

# def func(x: int, y: int) -> int:
#     print('hello')
#     return x + y


# res1 = func(10, 20)
# print(res1)
# print(res1 + func(50, 50))  # 130
# res = func(10, 20)
# print(res)

# DRY - Don't Repeat Yourself

# def func():
#     for i in range(1, 10):
#         print(i)

# func()

# return - ключевое слово для возвращения результата/сохранения значения в памяти, точка выхода из функции/точка остановки
# если return не указан - по умолчанию в функции стоит return None

# создание функции
# def имя_функции(параметры/локальные_переменные):
#     тело функции

# вызов функции
# имя_функции(аргументы)


def func1(a, b=10):
    return a + b


func1(20)  # 30
func1(20, 70)  # 90

# параметры бывают: обязательные и необязательные(имеют значение по умолчанию)

# def wrong_func(a=10, b, c):
    # ...


# аргументы бывают: позиционные и именованные
# def func2(a, b):
#     print(a, b)


# func2(10, 20)
# func2(a=10, b=20)
# func2(b=20, a=10)

# def func3(*, name1, name2):
#     print(name1, name2)


# func3(name1='Akzhol', name2='Bekzat')
# обязательные именованные аргументы


""" *args, **kwargs - arguments, keyword arguments """
# args - кортеж из позиционных аргументов
# kwargs - словарь из именованных аргументов


# def a_k(*args: tuple, **kwargs: dict):
#     print('ARGS', args)
#     print('KWARGS', kwargs)


# a_k(1, 2, 3, 4, a=1, b=2, c=3)
# a_k(1, 2, 3, 4, kwargs={'a': 1, 'b': 2, 'c': 3})


# from typing import Tuple

# def my_sum(*args: Tuple[int]) -> int:
#     # args (1, 2, 3, 4)
#     counter = 0
#     for num in args:
#         try:
#             counter += num
#         except TypeError:
#             continue
#     return counter


# res = my_sum(1, 2, 's', 3, 4)
# print(res)


# def func(s: str):
#     return s.upper()


# callback функция - функция, которую должна вызывать другая функция

def main_func(callback, *nums):
    return [callback(num) for num in nums]


def multiply(num):
    return num * 2


def divide(num):
    return num / 2


a = main_func(multiply, 2, 3, 4, 5)
# print(a)  # [4, 6, 8, 10]
b = main_func(divide, 2, 3, 4, 5)


# assert утверждение, [сообщение]
# assert 10 > 0
# assert 0 > 10, 'утверждение неверно'

# if not 0 > 10:
#     raise AssertionError('утверждение')

# def func5(num1, num2):
#     return num1 + num2


# def test_func5():
#     assert func5(10, 10) == 20


# test_func5()
