""" Кортеж """

# tuple() - неизменяемый список

t_1 = (1, 2, 3)
t_2 = 1, 2, 3

t_3 = 1,

days = [
    'понедельник',
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
    ]

# days.append('восмельник')

im_days = (
    'понедельник',
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
)

im_dict = (
    ('name', 'Zaynab'),
    ('age', 18)
)

dict_ = dict(im_dict)
# print(dict_)

nums = [1, 2, 3]
nums_2 = (1, 2, 3)

print(nums.__sizeof__())
print(nums_2.__sizeof__())

# print(dir(tuple))

# letters = ('a', 'b', 'c', 'a', 'b')
# print(letters.count('a'))
# print(letters.index('b', letters.index('b') + 1))


a, b, c = (1, 2, 3)
# Звездочный синтаксис
# *, **
names = ('Masha', 'Aliya', 'Kirill', 'Aibek')
# print(names)
# print(names[0], names[1], ...)
# print(*names, sep='\n')

# pow(10, 20, 30)
# pow(base=10, exp=20, mod=30)
# nums = {'base': 20, 'exp': 30}
# print(pow(**nums))

# nums = [{'base': 20, 'exp': 30}, {'base': 20, 'exp': 30}, {'base': 20, 'exp': 30}, {'base': 20, 'exp': 30}, {'base': 20, 'exp': 30}]
# for n in nums:
#     print(pow(**n))
    # print(pow(n['base'], n['exp']))


# *a1, b2, c3 = (1, 2, 3, 4, 5, 6)
# print(a1, b2, c3, sep='\n')


""" sets """
# set() - изменяемый, итерируемый, неиндексируемый, неупорядоченный. Содержит только уникальные, неизменямые значения.

fake_set_ = {}
print(type(fake_set_))

real_set = set()

# set_1 = {1, 2, 3, 4}
# print(set_1)

# from string import ascii_uppercase

# a = set(ascii_uppercase)
# print(a)

# b = {'b', 'b'}
# print(b)

# a = [1, 2, 1, 1]
# print(list(set(a)))

# c = {1, 2, 3, [4, 5]}  # Error
# d = {[1, 2]: 'asdfs'}  # Error

# m = {True, 1, 0, False}
# print(m)

# c = {8, 6, 7, 4, 5, 4}
# print(c)

# fruits_1 = {'apple', 'banana', 'peach'}
# fruits_2 = {'kiwi', 'banana', 'tangerin'}

# result = fruits_1.intersection(fruits_2)
# print(result)
# print(fruits_1.difference(fruits_2))
# print(fruits_2.difference(fruits_1))

"""  
Задание 13
Написать программу, которая будет принимать от пользователя числа через запятую, без пробелов.
числа поместить в список list_ и вывести в отсортированном виде.
Числа переданные во вкладке INPUT сохраняются в строковом типе данных.

Поэтому, к примеру, для чисел 15,364,27,2 отсортированный список будет выглядеть так:
['15', '2', '27', '364']
"""

'15,364,27,2'
# inp1 = input().split(',')
# res = []
# for i in inp1:
#     res.append(int(i))
# inp1.sort(key=int)
# print(inp1)

# ['15', '2', '27', '364']

"""  
Объявите переменные string1 и string2 со значением в виде любой строки.
Выведите значение данных переменных используя интерполяцию строк.
Необходимо использовать функцию print() только один раз.
К примеру, если в string1 хранится строка "Hello",
а в переменной string2 хранится строка "World"
Вывод:
Hello World
"""
# string1 = 'asdfasdf'
# string2 = 'fhdfkgfd'
# print(f'{string1} {string2}')


"""  
Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
Вводить в порядке x1, y1, x2, y2
"""

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
