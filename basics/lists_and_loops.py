# """ list, loops: for, while, iterable """

# # list() - список - изменяемый, упорядоченный, индексируемый, итерируемый тип данных.
# # служит для хранения набора элементов

# nums = [1, 2, 3, 4, 5]

# all_data_types = [1, 'string', True, False, [1, 2], None, {'a': 10}, {1, 2}, (1, 2, 3)]

# nums[0]  # 1
# nums[1]  # 2

# list_ = [1, 2, [3, 4, [5, 6]]]
# inner_list = list_[2]  # [3, 4]
# inner_list[0]  # 3
# inner_list[2][0]  # 5

# # Коллекция - какой-либо тип данных, который содержит набор элементов

# """ Методы списков """

# """
# 1) Добавление элементов в список
# """
# list_1 = [1, 2]
# list_1.append(3)
# print(list_1)

# list_1.insert(0, -90)
# print(list_1)

# list_2 = [10, 20]
# list_1.extend(list_2)
# # print(list_1)
# list_1.extend('hello')
# # print(list_1)

# # list_1[0] = 'apple'
# # print(list_1)

# # 'hello'[0] = 'b' # Error

# """
# 2) Удаление элементов
# """
letters = ['a', 'b', 'c', 'd']
# letters.remove('c')
# print(letters)

# deleted_element = letters.pop(1)
# print(deleted_element)
# print(letters)

# letters.clear()

# del letters[0]

""" сортировка и копирование списка """
# list_3 = [5, 3, 6, 8, 9, 1]
# list_3.sort()
# print(list_3)

# sorted_list = sorted(list_3)
# print(list_3)
# print(sorted_list)

# list_3.reverse()
# reversed(list_3)

# list_of_names = ['Kolya', 'Michael', 'Alex', 'Ura']
# list_of_names.sort(key=len, reverse=True)
# print(list_of_names)

# nums = [1, 2, 3]
# nums2 = nums.copy()

# nums2.append(4)
# print(nums)

nums_1 = [1, 2, [3, 4]]
nums_2 = nums_1.copy()

nums_2[2].append(5)
# print(nums_2)
# print(nums_1)
print(nums_1[2] is nums_2[2])  # True

from copy import deepcopy
real_copy = deepcopy(nums_1)
print(nums_1[2] is real_copy[2])  # False
