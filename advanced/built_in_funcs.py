""" Встроенные функции """


"""  
map()
filter()
reduce()*
zip()
enumerate()
all()
any()
"""





def func(x, y):
    return x + y


lambda x, y: x + y
func2 = lambda x, y: x + y


func(10, 20)
func2(10, 20)

# lambda - ключевое слово для создания анонимных функций (lambda параметры: выражение)


# map(func, iter) - применяет func ко всем элементам iter

list_1 = [1, 2, 3, 4]
# list_2 = []
# for i in list_1:
#     list_2.append(i * 2)
# print(list_2)  # [2, 4, 6, 8]


# list_3 = map(lambda x: x * 2, list_1)
# print(list(list_3))
# print(tuple(list_3))
# list_4 = (i * 2 for i in list_1)
# print(list(list_4))
# print(tuple(list_4))


# filter(func, iter) - фильтрует по условию функции

# list_1 = [7, 5, 3, 2, 9, 8]
# list_2 = []
# for i in list_1:
#     if i % 2 == 0:
#         list_2.append(i)
# print(list_2)  # [2, 8]

# def func(x):
#     return x % 2 == 0


# list_3 = filter(lambda x: x % 2 == 0, list_1)
# print(list(list_3))
# print(dir(list_3))
# print(tuple(list_3))

# for i in list_3:
#     print(i)

# for i in list_3:
#     print(i)


# zip(*iters)

# ages = [10, 20, 18]
# names = ['Lesha', 'Katya', 'Akylbek', 'Aliya']
# city = ['Bishkek', 'Moscow', 'Osh']

# res = zip(names, ages, city)
# print(list(res))
# print(dict(res))


# enumerate(iter) - нумерует элементы итер
# res2 = enumerate('names')
# print(list(res2))

# list_1 = [1, 2, 3, 4]
# for index, value in enumerate(list_1):
#     if value % 2 == 0:
#         list_1[index] = 'hello'
# print(list_1)


# all()
# all([1, 2, 3, 5, 0])  # False

# res = map(lambda x: x - 10, [40, 20, 10, 1])
# print(all(res))  # False


# any()
any([0, 0, 0, 1])  # True
any([0, 0, 0])  # False

'superpaSsword'
# def check_password(password: str):
#     if any(i.isupper() for i in password):
#         return 'Ok!'
#     else:
#         raise ValueError('Ваш пароль должен содержать хотя бы один символ верхнего регистра')


# print(check_password('mysuperPass'))


# def map_(func, iterable):
#     for i in iterable:
#         yield func(i)


# res = map_(lambda x: x * 2, range(5))
# print(res)  # 0
# print(list(res))
# print(tuple(res))

# def func():
#     return 10

# func()


# Итерируемые объекты - объекты, к которым применим цикл for
# list, str, dict, set, tuple

# for i in map(lambda x: x * 2, range(10)):
#     ...

# nums = [1, 2, 3]
# iter_nums = iter(nums)
# while True:
#     try:
#         print(next(iter_nums))
#     except StopIteration:
#         break


# def gen():
#     yield 1
#     yield 2
#     yield 3

# a = gen()
# next(a)  # 1
# next(a)  # 2
# next(a)  # 3


# eval()
# exec()

code = "print(10)"
eval(code)


big_code = """
b = 10
for i in range(b):
    print(i ** i)
"""

exec(big_code)
