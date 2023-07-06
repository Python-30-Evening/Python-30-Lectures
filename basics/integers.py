# int - неизменяемый тип данных. Обозначает целые числа
int()
int_num = 10

# float() - обозначает числа с плавающей точкой
float_num = 10.05


""" Операции с числами """
num1 = 10
num2 = 2

num1 + num2  # 12
num1 - num2  # 8
num1 * num2  # 20
num1 / num2  # 5.0
num1 // num2  # 5
num1 ** num2  # 100
num1 % num2  # 0
num1 % 3  # 1

a = 10
b = 20
c = 30

a, b, c = 10, 20, 30


""" Операторы сравнения """
num3 = 20
num4 = 30

num3 > num4  # False
num3 < num4  # True
num3 == num4  # False
num3 != num4  # True - неравенство
num3 >= num4  # False - больше или равно
num3 <= num4  # True - меньше или равно


10 % 2 == 0  # True


# num = 50
# num + 20
# print(num)  # 50

# num = 50
# num += 20  # num = num + 20 - перезапись
# print(num)  # 70


# result = 10 + 10.50
# print(result)

# 10.50 -> '10'+'.'+'50'
# result = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
# print(result)

# from decimal import Decimal

# result = Decimal('0.1')
# result += Decimal('0.1')
# result += Decimal('0.1')
# result += Decimal('0.1')
# result += Decimal('0.1')
# result += Decimal('0.1')
# result += Decimal('0.1')
# print(result)


""" Функции для работы с числами """
f_num = 10.5
f_num2 = 10.6
f_num3 = 10.4

# print(round(9.5))  # 10
# print(round(f_num))  # 10
# print(round(f_num2))  # 11
# print(round(f_num3))  # 10
# print(round(3.14678236871234, 2))  # 3.15


# abs()
abs(4)  # 4
# _______0____4___
abs(-5)  # 5
# -5_____0_____


# pow(base, exp, [mod]) -> base ** exp [% mod]

# num = 10
# help(num)

# print(dir(num))
# 10 + 10
# (10).__add__(10)

# a = 10
# b = 20
# a + b
# print('До ошибки')
# # m + a
# print('После ошибки')
# a + b
# -> s8a6d8 asd7f78as sadf68a asd6f8f -> 001010001000100010010
