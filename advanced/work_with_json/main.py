""" JSON """
# JSON - JavaScript Object Notation - переводчик между языками программирования / формат файлов для обмена данными между языками программирования

import json

# сериализация - перевод из python в json
# десериализация - перевод из json в python


teapot = {
    'title': 'Teapot ARG',
    "price": 1500,
    "in_stock": True,
    "description": "cool teapot"
}

import json

# with open('db.json', 'w') as db:
#     json_res = json.dumps(teapot, indent=4)
#     # print(json_res)
#     # print(type(json_res))
#     db.write(json_res)


# with open('db.json', 'r') as db:
#     res = db.read()
#     python_obj = json.loads(res)
#     print(python_obj)
#     print(type(python_obj))


# python                 json
# dict                   object
# list                   array (массив)
# str                    string
# int                    number
# True/False             true/false
# None                   null


laptops = [
    {
        "title": "ASUS",
        "price": 100000,
        "ssd": None,
        "hdd": "Samsung"
    },
    {
        "title": "Acer",
        "price": 1034340,
        "ssd": "Toshiba",
        "hdd": "LG"
    },
    {
        "title": "HP",
        "price": 1003232,
        "ssd": None,
        "hdd": "Samsung"
    },
]

with open('laptops.json', 'w') as db:
    json.dump(laptops, db, indent=4)

with open('laptops.json', 'r') as db:
    res = json.load(db)
    print(res)


# phone = {
#     "title": "Samsung",
#     "price": 123123,
#     "description": "Классный телефон"
# }

# print(json.dumps(phone, ensure_ascii=False))

# from urllib.request import urlopen

# json_cat_fact = urlopen('https://catfact.ninja/fact')
# res = json_cat_fact.read()  # str
# python_obj = json.loads(res)  # dict
# print(python_obj)
# print(python_obj['fact'])
# print(python_obj['length'])
