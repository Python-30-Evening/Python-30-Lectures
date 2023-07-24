""" Области видимости и пространства имен """

x = 10
print(x)


y = 20
def func():
    print(y)


func()


# def func2():
#     c = 30


# print(c)

# Local (локальное)
# Enclosed (замнкнутое)
# Global (глобальное)
# Built-in (встроенное)

# Имена из локальной области не доступны в глобальной, а глобальные доступны везде

global_ = 'глобальная переменная'


def func():
    local_ = 'локальная переменная'
    def inner_func():
        local_too = 'тоже локальная переменная'
        def inner_inner_func():
            local_local_too = 'value'


# def my_func():
#     global var
#     var = 10


# my_func()
# print(var)


# def func1():
#     var = 10
#     def inner_func():
#         nonlocal var
#         var = 20
#     inner_func()
#     print(var)


# func1()

# Старайтесь писать такие функции, которые не зависят от глобальных переменных

names = ['Alesha', 'Masha', 'Sasha']
# Bad practice
# def print_names():
#     for user in users:
#         print(user)

# print_names()

# Good practice
# def print_names(users):
#     for user in users:
#         print(user)

# print_names(names)


# globals() - возвращает список глобальных имен
# locals() - возвращает список имен той области, где была вызвана


# def test_func():
#     a = 10
#     b = 20
#     print(locals())

# test_func()

# print(locals())
# print(globals())

# globals().update({'new_name': 50})
# print(new_name)

# b = 30
# b = 50
# {'b': 30, 'b': 50}

# m: int = 10
# print(globals())

# Модуль - файл с кодом
# from crud.crud import big_code
# from users.users import big_code2


# def main():
#     big_code()
#     big_code2()


# if __name__ == '__main__':  # Точка входа в программу
#     # место откуда ваша программа запускается
#     print('Programm started')
#     main()


# def hello_world():
#     print('hello world')
#     print(__name__)


# if __name__ == '__main__':
#     hello_world()

# import users.users

# print(users.users.__package__)

# from users.users import big_code2
# from users.models import super_big_code

# from users import big_code2, super_big_code
# big_code2()

# Пакет - директория, который состоит из модулей и в котором есть модуль __init__.py


# class B:
#     a = 10

# print(B.a)
