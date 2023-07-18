""" Генераторы, итераторы """

# comprehension - короткий, более быстрый способ генерации коллекций

# list_ = []
# for i in range(1, 6):
#     list_.append(i)

# print(list_)

# list_1 = [i for i in range(1, 6)]
# print(list_1)

# list_2 = [i * 2 for i in range(1, 6)]
# print(list_2)

# [действие for переменная in итерируемый_объект]

# gen = (i for i in range(1, 6))
# print(type(gen))

# print([*gen])

# list3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list3.append(i)

# print(list3)

# list4 = [i for i in range(1, 11) if i % 2 == 0]
# print(list4)

# list5 = []
# TODO: записать в список числа от 1 до 10, при этом числа кратные 2(num % 2 == 0) увеличить на 100, остальные увеличить на 400
# for i in range(1, 11):
#     if i % 2 == 0:
#         list5.append(i + 100)
#     else:
#         list5.append(i + 400)

# print(list5)

# res = 'apple' if 5 > 0 else 'grape'

# list7 = []
# for i in range(1, 11):
#     list7.append(i + 100) if i % 2 == 0 else list7.append(i + 400)

# list6 = [i + 100 if i % 2 == 0 else i + 400 for i in range(1, 11)]


# TODO: записать в список числа от 1 до 15, при этом числа кратные 2(num % 2 == 0) увеличить на 100, остальные увеличить на 400, только для тех чисел, которые также кратны 3(num % 3 == 0)
list8 = []
for i in range(1, 16):
    if i % 3 == 0:
        if i % 2 == 0:
            list8.append(i + 100)
        else:
            list8.append(i + 400)

list9 = [i + 100 if i % 2 == 0 else i + 400 for i in range(1, 16) if i % 3 == 0]

# [действие for переменная in итерируемый_объект]
# [действие for переменная in итерируемый_объект if условие]
# [тернарный оператор for переменная in итерируемый_объект]
# тернарный оператор - действие if условие else действие2
# [тернарный оператор for переменная in итерируемый_объект if условие]


names = {
    "Nargiza": 18,
    "Kanat": 25,
    "Aktilek": 30
}
# new_names = {}
# for key, value in names.items():
#     new_names.update({key: value + 1})

# print(new_names)
# new_names = {key: value + 1 for key, value in names.items()}
# print(new_names)

# y = {}
# for key, value in names.items():
#     if value < 20:
#         y.update({key: value})

# print(y)
# y2 = {key: value for key, value in names.items() if value < 20}
# print(y2)

# data = {
#     "aigul": {"age": 19, "is_alive": True},
#     "misha": {"age": 24, "is_alive": False},
#     "ruslan": {"age": 60, "is_alive": True},
# }

# result = {}
# TODO: найти погибших и старше 20 лет и поместить их в result
# for key, value in data.items():
#     for inner_key, inner_value in value.items():
#         if value['age'] > 20 and not value['is_alive']:
#             result.update({key: value})

# print(result)


data = {
    "aigul": {"age": 19},
    "misha": {"age": 24},
    "ruslan": {"age": 60},
}

# result = {}
# for key, value in data.items():
#     for inner_key, inner_value in value.items():
#         result.update({inner_value: {inner_key: key}})

# print(result)

# result = {inner_value: {inner_key: key} for key, value in data.items() for inner_key, inner_value in value.items()}
# print(result)


# gen = (i for i in range(1, 6))
# print(type(gen))

# print([*gen])
# print(list(gen))
# print(tuple(gen))

# a = [1, 2, 3, 4]

# nums = (i for i in range(1, 1000000000))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# list_1 = range(1, 100)
# list_1 = (i for i in range(1, 100))
# a = list(list_1)
# b = tuple(list_1)
# print(a)
# print(b)
 