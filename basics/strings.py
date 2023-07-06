""" строки """

# str()

# string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

string = 'Hello'
string2 = "Hello"
doc_string = """ Very
long
long
text
"""
doc_string2 = '''
long string
'''

greeting = " I'am student "
greeting2 = 'I\'am student'  # Экранирование

str1 = "Hello"
str2 = "world"
print(str1 + str2) # Helloworld - конкатенация - склеивание строк

str1 * 3  # HelloHelloHello


""" Функции и методы строк """
name = "Bekzat Tigranov"

# print() - это функция - не привязан к типу

# name.lower() - это метод - привязан к типу

print(name.lower())
print(name.upper())
print("aLIYA mARATOVA".title())
print('aLIYA mARATOVA'.capitalize())
print(name.swapcase())

print(name.split())
