""" Циклы """

# Цикл - многократное повторение участка кода

# Итерация - повторение действия

# Итерируемый объект - объект, к которому применим цикл for

nums = [1, 2, 3]
# nums[0]
# nums[1]
# nums[2]

# DRY - Don't Repeat Yourself
# for num in nums:
#     print(num)

# для элемента внутри итерируемого_объекта:
    # сделай действие над элементом

# итерируемые объекты:
# 1) list
# 2) str
# 3) dict
# 4) tuple
# 5) set

# for - цикл, который работает пока не кончатся элементы внутри объекта

# for i in "bottle":
#     print(i)

# string = 'HasasdEsdvadsbLasdfasdLsadfasdfO'
# res = ''
# for i in string:
#     if i.isupper():
#         res += i
# print(res)

# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in nums:
#     print(i)
#     for j in i:
#         print(j)


# names = ['Marina', 'Alex', 'Aliya']
# for name in names:
#     if name == 'Alex':
#         break
#     print(f'Входите {name}')

# names = ['Marina', 'Alex', 'Aliya', 'Misha']
# for name in names:
#     if name == 'Alex':
#         continue
#     else:
#         print(f'Входите {name}')

a = [1, 2, 3]
# print(dir(a))
print('__iter__' in dir(a))
print('__iter__' in dir(10))
