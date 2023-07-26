""" Декоратор """

# Декоратор - функция высшего порядка, в качестве аргумента принимает другую функцию для расширения ее функционала и возвращает дополненную функцию при этом не затрагивая тело принимаемой функции

# num = 10
# string = 'hello'

# def func():
#     return 'result'

# test_func = func

# test_func()  # 'result'
# print(dir(func))
# print(func.__name__)


# def main_func(func):
#     func('Hello world')

# main_func(print)
# main_func(len)  # 11
# from datetime import date, datetime

# def register_user():
#     print(datetime.now())
#     ...

# def func2():
#     print(datetime.now())
#     ...

# def func3():
#     print(datetime.now())
#     ...

# def func4():
#     print(datetime.now())
#     ...


# def decorator(func):
#     def wrapper():
#         print(datetime.now())
#         return func()
#     return wrapper


# @decorator
# def func5():
#     return [i for i in range(10)]


# @decorator
# def func6():
#     return 'result'


# print(func5())
# print(func6())
# from datetime import datetime

# def timer(func):
#     def wrapper():
#         start = datetime.now()
#         res = func()
#         end = datetime.now()
#         print(end - start)
#         return res
#     return wrapper

# @timer
# def get_list():
#     return [i * 2 for i in range(1_000_000)]

# get_list()


# def main_func():
#     def inner_func():
#         return 10 * 2
#     return inner_func

# inner_func = main_func()
# print(inner_func)
# # print(inner_func)
# print(inner_func())  # 20


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         print('До выполнения функции')
#         res = func(*args, **kwargs)
#         print(res)
#         print('После выполнения функции')
#         return res
#     return wrapper


# @decorator
# def test_func(x, y):
#     return x * y

# @decorator
# def a_func(a, b, c, d):
#     return a, b, c, d


# test_func(10, 2)  # 20
# a_func(10, 20, 30, 40)  


# def call(times: int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator


# @call(times=5)
# def test_func():
#     print('Hello world')


# test_func()


def deco1(func):
    def wrapper(*args, **kwargs):
        print(f'Вызвана {func.__name__} #1')
        res = func(*args, **kwargs)
        return res + ' deco1'
    return wrapper


def deco2(func):
    def wrapper(*args, **kwargs):
        print(f'Вызвана {func.__name__} #2')
        res = func(*args, **kwargs)
        return res + ' deco2'
    return wrapper


# @deco1
# @deco2
# def hello(name):
#     return f'Hello {name}'



# hello = deco1(hello)
# print(hello('Kanybek'))

# from math import sqrt

# sqrt = deco1(sqrt)
# print(sqrt(25))


"""
Напишите декоратор call_function, который печатает перед вызовом полученной функции строку:

 Вызываю функцию <имя_функции>
Затем следует вызов функции. После вызова функции должна печататься строка:

 "Вызов функции <имя_функции> прошёл успешно"
Ввод:

@call_function
def first():
    print("hello world")
    return "hello world"
first()
Вывод:

Вызываю функцию first
hello world 
Вызов функции first прошёл успешно 
"""


def call_function(func):
    def wrapper(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__}')
        func(*args, **kwargs)
        print(f'Вызов функции {func.__name__} прошёл успешно')
    return wrapper


@call_function
def first():
    print("hello world")
    return "hello world"


first()
