# """ строки """

# # str()

# # string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

# string = 'Hello'
# string2 = "Hello"
# doc_string = """ Very
# long
# long
# text
# """
# doc_string2 = '''
# long string
# '''

# greeting = " I'am student "
# greeting2 = 'I\'am student'  # Экранирование

# str1 = "Hello"
# str2 = "world"
# print(str1 + str2)  # Helloworld - конкатенация - склеивание строк

# str1 * 3  # HelloHelloHello


# """ Функции и методы строк """
# name = "Bekzat Tigranov"

# # print() - это функция - не привязан к типу

# # name.lower() - это метод - привязан к типу

# print(name.lower())
# print(name.upper())
# print("aLIYA mARATOVA".title())
# print('aLIYA mARATOVA'.capitalize())
# print(name.swapcase())
# print(name.split())


# """ Индексация и срезы """

# # Индекс - порядковый номер элементов строки (контейнеров).
# # В программировании индексация начинается с 0

# "hello"
# # 0 1 2 3 4

# " "
# "hello world"
# # 012345 6

# string = "apple"
# print(string[1])  # p
# print(string[3])  # l

# print(string[4])
# print(string[-1])
# print(string[len(string)-1])
# print(string[32456])
# Синтаксический сахар - облегченный вид синтаксиса

# num = str(234567)
# print(int(num[2]))


# string2 = "hello"
# print(string2[0:3])
# string2[start:stop:step]
# print(string2[0:4:2])
# print(string2[2:])
# print(string2[::-2])
# print(string2[11234:12341234:])


""" Форматирование / интерполяция строк """
# "Hello, ______"
# Форматирование строк - подстановка переменных в строку/создание динамической строки

# name = input('Введите имя: ')
# date = input('Введите дату: ')

# a1 = "Привет, %s Cегодня %s число" % (name, date)
# print(a1)
# a2 = "Hello, {n} Today {d}".format(n=name, d=date)
# print(a2)
# a3 = f"Hello, {name}! Today {date}"
# print(a3)
# from datetime import datetime
# a4 = f"Today {datetime.now()}"
# print(a4)

""" Экранирование """

# string = "Hello \nworld"
# print(string)
# string = "Hello \tworld"
# print(string)

# path = "C:\\Users\Photos\\new_games\\tables"
# path2 = r"C:\Users\Photos\new_games\tables"
# print(path)
# print(path2)


# str1 = "hkllo"
# str2 = "hello"
# # print(str1 == str2)
# print(str1 > str2)


# id 
# a = 10
# b = 10
# print(a is b)

# c = 257
# n = 257
# print(c is n)
# print()
