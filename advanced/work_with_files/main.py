""" Работа с файлами """

# Файлы бывают:
# 1. Текстовые
# 2. Бинарные (картинки, видео и тд)

# Файлы можно
# Читать
# Записывать

# open(путь_до_файла, режим_работы_с_файлом) - открывает файл, возвращает специальный тип данных для работы с файлом

"""
r - read - чтение. Исключение, если файла нет (по умолчанию)
w - write - перезапись. Если файла не существует - создает файл
x - exclusive - создает и записывает в файл. Исключение если файл уже существует
a - append - дозапись данных
+
r+, w+ - запись и чтение одновременно
b - работа с бинарными файлами
t - работы с текстовыми файлами
wb
rb
"""

# file = open('ex1.txt', 'r')
# # print(type(file))
# # print(file.read()) - читает весь файл
# # print(file.readline()) - читает файл построчно
# # print(file.readline())
# # print(file.readlines()) - читает весь файл и возвращает в виде списка
# file.close()

# file = open('ex1.txt', 'r')
# for line in file:
#     print(line)
# file.close()

# file1 = open('ex1.txt')
# print(file1.read(), "1")
# print(file1.tell())
# file1.seek(0)
# print(file1.read(), "2")
# file1.close()

# file = open('ex1.txt')
# raise Exception
# file.close()

# try:
#     file = open('ex1.txt')
# finally:
#     file.close()

# with - контекстный менеджер - открывает рабочий поток, который закроется в любом случае (отлавливает исключения)

# with func() as name:
#     name

# file = open(..., ...)
# with open('ex2', 'w') as file:
#     file.write('bottle\n')
#     file.write('water')

# with open('ex2', 'w') as file:
#     file.write('banana')


# with open('ex2', 'a') as file:
#     file.write('strawberry')

# with open('ex3', 'x') as file:
#     ...

# with open('ex4', 'w+') as file:
#     file.write('new string')
#     file.seek(0)
#     print(file.read())

# with open('ex5', 'w') as file:
#     with open('ex5', 'r+') as file:
#         file.write('another string')
#         file.seek(0)
#         print(file.read())

# with open('ex6', 'w') as file:
#     nums = [str(num) + "\n" for num in range(1, 11)]
#     file.writelines(nums)



