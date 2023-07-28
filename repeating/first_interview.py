# terminal - средство управления компьютером

# типов данных - 8
# изменяемые:
# list, dict, set
# неизменяемые:
# int, tuple, str, bool, None

# iterable:
# list, dict, set, tuple, str

# word = "Apple"
# new_word = word.replace('l', 'o')
# print(word)  # "Apple"
# print(new_word)  # "Appoe"


# dict
# d = {"key": "value"}
# d.update({'new_key': 'new_value'})
# print(d)

# person = {
#     "name": "Ken",
#     "age": 25,
#     "education": {
#         "organization": "KRSU",
#         "date": "2018-2022",
#     },
#     "license": {
#         "name": "Mashina",
#         "gos_number": {
#             "region": "08",
#             "number": "748",
#             "letters": 'ABC'
#         }
#     }
#     }


# name = person["name"]
# name2 = person.get("name", "Нет такого ключа")
# print(name)
# print(name2)

# edu = person['education']
# org = edu['organization']
# print(edu)
# print(org)
# print(person['education']['organization'])
# reg = person['license']['gos_number']['region']
# print(reg)
# reg2 = person.get('license').get('gos_number').get('region')
# print(reg2)
# person['license']['name'] = 'BarbieCar'


# nums = [1, 2, 3, 4]

# nums[0] * 2
# nums[1] * 2
# ...
# for num in nums:
#     res = num * 2
# for i in nums:
#     print(i)

# nums = [1, 2, 3, 4]

# index = 0
# while index < len(nums):
#     print(nums[index])
#     index += 1


# functions - переменная, которая хранит блок кода

users = ['Nazira', 'BAgira', 'Barbie', 'Ken']
result = []
for i in users:
    result.append(i.upper())

print(result)


# def upper_names(users):  # параметры
#     result = []
#     for i in users:
#         result.append(i.upper())

#     return result


# res = upper_names(['Aykol', 'Adilet', 'Ilias'])
# print(res)
# upper_names(['anothername', 'name2', 'name3'])


# def func_name():
#     ...

# def func():
#     print(10)

# def func2():
#     a = 10
#     b = 20
#     return b + a


# n = [1, 2, 3]
# n.append(4)
# print(n)

# def func3():
#     return 10
#     print('hello world')

# func3()
# def test_func():
#     print('test func working')
#     return 10

# def func4():
#     try:
#         return test_func()
#     except:
#         return 20
#     else:
#         return 30
#     finally:
#         return 40


# res = func4()
# print(res)  # 40


def decorator(func):  # декоратор
    def wrapper(*args, **kwargs):  # обертка
        print('До вызова функции')
        func()
        print('После вызова функции')
    return wrapper

# def decorator2(func):  # декоратор
#     def wrapper(*args, **kwargs):  # обертка
#         print('До вызова функции2')
#         func()
#         print('После вызова функции2')
#     return wrapper


# @decorator
# @decorator2
# def simple_func():
#     print('Hello world')


# @decorator
# def simple_func2():
#     print('Goodbye world')


# simple_func()


# print(a)
# NameError

# [1, 2, 3][10]
# IndexError

# {'key': 'value'}['asdf']
# KeyError


# code = """
# a = 10
# print(a)
# """

# exec(code)
