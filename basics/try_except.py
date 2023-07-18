""" try except - ошибки и исключения """

# TypeError
# ZeroDivisionError
# AttributeError

# SyntaxError

# исключения - те случаи, которые можно избежать/исключить
# ошибки - случаи, которые избежать нельзя


from sys import stderr, stdout


ValueError
# int('asdfasdf')
# from math import sqrt
# sqrt(25)
# sqrt(-60)

# a = 10
# b = 20
# print(c)
NameError

ZeroDivisionError
# 10 / 0

KeyError
# d = {'a': 10}
# d['b']

# IndexError
# a = 'string'
# a[21345]


SyntaxError
# for i in range(1:
#                asdfsdf


# try:
    # действие с потенциальным исключением
# except:
     # действие если в блоке try произошло исключение
# else:
     # если try прошел успешно
# finally:
    # работает всегда


# a = 10
# b = 20
# try:
#     print(a / "string")
# except:  #  голое исключение
#     print('Не получилось провести операцию')

# print('весь остальной код...')


# try:
#     list.update
#     10 / 0
# except (ZeroDivisionError):
#     print('нельзя делить на ноль')
# except AttributeError:
#     print('неправильный метод')


# raise Exception('вызвано исключение')
speed = 0
try:
    set_speed = int(input('Enter speed '))
    if set_speed > 200 or set_speed < 10:
        raise ValueError('Недопустимая скорость')
    else:
        speed = set_speed
except ValueError as e:
    print('Вы ввели не число')
    with open('errors.log', 'w') as file:
        print(e, file=file)
        print(e.__traceback__.tb_frame, file=file)
    # Log, Логи
