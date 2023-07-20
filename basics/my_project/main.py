""" Виртуальное окружение - изолированное пространство для работы с библиотеками """

# python3 -m venv <venv-name> - создать окружение
# . <venv-name>/bin/activate - активация окружения
# deactivate - деактивация окружения

# pip - команда для работы с библиотеками
# pip install <lib-name>
# pip uninstall <lib-name>
# pip freeze - список установленных библиотек

# import cowsay

# cowsay.fox('Hello world')
from typing import List

database = []
current_user = {}


def register_user(db: list, username: str, password: str) -> None:
    user = {
        "username": username,
        "password": password
    }
    db.append(user)
    print(user['username'], 'successfully registered!')


def login(db: List[dict], current_user: dict, username: str, password: str):
    for user in db:
        if user['username'] == username:
            if user['password'] == password:
                current_user['username'] = username
                return (f'Welcome, {username}!')
            else:
                return 'Invalid data'
    else:
        return 'User not found'
    

register_user(database, 'admin', 'mypassword')
print(database)
res = login(database, current_user, 'admin', 'wrongpassword')
print(res)
print(current_user)
