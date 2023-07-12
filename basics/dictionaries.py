# """ словари """

# # dict() - изменяемый, итерируемый, упорядоченный (с версии python 3.6), неиндексируемый (ключи вместо индекса), нужен для описания объекта

# # Состоит из пар: ключа и значения

# # apple - яблоко
# # Имя - Марат

# passport = {
#     'name': 'Marat',
#     'age': 17,
#     'last_name': 'Akbarov',
#     'license': {
#         'category': 'B',
#         'date': '12.12.2012'
#     }
#     }
# a = passport['name']  # 'Marat'
# # print(a)
# # passport['gender']  # KeyError
# passport['gender'] = 'M'
# # print(passport['gender'])
# passport['license']['category']  # 'B'


# # Ключами могут быть только неизменямые типы данных, значением может быть любой тип данных
# # a = {1: 'asdf', [1, 2]: 'asdf'}
# # a[[1, 2]]

""" словари с циклами """
person = {
    'name': 'Aliya',
    'last_name': 'Erkinbekova',
    'age': 18
}

# for i in person:
#     print(i)

# person['name']
# for key in person:
#     print(person[key])

# v = person.values()
# k = person.keys()
# it = person.items()
# print(v, k, it, sep='\n')

# for v in person.values():
#     print(v)


# for item in person.items():
#     print(item)
#     print(f'{item[0]} = {item[1]}') # Not Ok

# a, b, c = 1, 2, 3
# name, last_name = ['Aliya', 'Erkinbekova']
# print(name)
# print(last_name)

# for key, value in person.items():
#     print(f'{key} is {value}')


# list_ = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for v1, v2, v3 in list_:
#     print(v1, v2)

# print(list(person.items())[0])


""" Методы словарей """
"""  
1) Добавление элементов
"""
movie = {
    'title': 'Зеленая книга',
    'date': '11.09.2018',
    'genres': ['comedy', 'drama']
}

movie['producer'] = 'Peter'
movie.update({'actor': 'Viggo'})
movie.update([['budget', 23_000_000]])
# print(movie)
# res = movie.setdefault('title')
# print(res)
res2 = movie.setdefault('description', 'Очень крутой фильм')
# print(res2)
# print(movie)

""" Удаление элементов """
el = movie.pop('date')
# print(el)
# print(movie)

# el2 = movie.pop('oscar', 'Ключ не найден')
# print(el2)

# el3 = movie.popitem()
# print(el3)

# movie.clear()
