# bool() - неизменяемый, имеет всего 2 значения True/False
# под капотом - True - 1, False - 0

# True -> 1
print(int(True))  # 1
res = True + 3  # 4

# truthy, falsy
# bool()
bool(10)  # True - truthy
bool(0)  # False - falsy

bool("apple")  # True
bool("")  # False
bool(" ")  # True

bool(None)  # False

# if условие:
#     действие если условие = True

# if 10 > 5:
#     print('Ok')

# if 5 > 10:
#     print('Ok 2')

# msg = input()
# if msg:
#     print(msg)

# weather = 'жарко'
# if weather == 'жарко':
#     print('надену футболку')
# else: # Ok
#     print('надену куртку')


# if weather == 'жарко':
#     print('1')
# elif weather != 'жарко': # Not ok
#     print('2')


""" and, or, not """
# age = 18
# if age >= 18 and age < 35:
#     print('Enter')

True  # True
False  # False

False and False  # False
False and True  # False
True and False  # False
True and True  # True
1 and 0  # 0
"" and "apple"  # ''
res = "apple" and "world"  # "world"
# print(res)

True or False  # True
False or True  # True
False or False  # False
True or True  # True
1 or 0  # 1
# res = 2 or 5  # 2
# print(res)

res = 10 or print("20")  # 10

(True and True) or (False and False)  # True

""" Тернарный оператор """
age = 18
# if age > 15:
#     print('Hello')
# else:
#     print('Goodbye')

# print('Hello') if age > 15 else print('Goodbye')
# msg = input()
# res = 'Cообщение получено' if msg else 'Сообщения нет'
# результат1 если условие = True иначе результат2

# number = 10
# match number:
#     case 10:
#         print('Ok')
#     case 5:
#         print('Not ok')
#     case _:
#         print('Не знаю как обработать')

"""  
Задание 1
Дано число введенное пользователем в переменной number.
Если число в переменной number больше 0 вывести True, иначе False.
Для проверки кода введите число в поле во вкладке INPUT.
Например, если в number ввели число:

21 
в результате получим:

True 
"""
# number = int(input())
# if number > 0:
#     print(True)
# else:
#     print(False)

# string = input()
# if len(string) > 5:
#     print(True)
# else:
#     print(False)
# print(True if len(string) > 5 else False)
# print(len(string) > 5)

# print(len(string := input()) > 5)

# mark = int(input())
# if mark >= 90:
#     print("Отлично, Ваша оценка 5!")
# elif mark >= 80:
#     print("Здорово, Ваша оценка 4!")
# elif mark >= 70:
#     print("Хорошо, Ваша оценка 3!")
# elif mark >= 60:
#     print("Вам стоит подучить материал")
# else:
#     print("Вы не сдали экзамен")

# num = int(input())
# res = chr(num)
# if res.isalpha():
#     print(f'Это буква "{res}"')
# else:
#     print(f'Это не буква, а символ "{res}"')


"""  
Дана строка string из 6-ти цифр записанных не через пробел.
Проверьте, что сумма первых трех цифр равняется сумме вторых трех цифр. Если это так - выведите 'да', в противном случае выведите 'нет'.
"""
string = "123123"
a, b, c, d, e, f = (
    int(string[0]),
    int(string[1]),
    int(string[2]),
    int(string[3]),
    int(string[4]),
    int(string[5]),
)
if a + b + c == d + e + f:
    print("yes")
else:
    print("not")
