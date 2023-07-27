from typing import List
from http import HTTPStatus as status
from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ['id', 'username', 'password']


database = []
current_user = {}


def generate_id():
    from uuid import uuid4
    return str(uuid4())[:4]


def register_user(db: list, username: str, password: str) -> None:
    user = {
        "id": generate_id(),
        "username": username,
        "password": password
    }
    db.append(user)
    table.add_row(user.values())
    return (user, status.CREATED)


def find_user(db: list, id: str):
    for user in db:
        if user['id'] == id.strip():
            return user, status.OK
    else:
        raise ValueError('User not found', status.NOT_FOUND)


def check_password(user, password):
    if not user['password'] == password:
        raise ValueError('Wrong password', status.BAD_REQUEST)
    return True, status.ACCEPTED


def login(db: list, current_user: dict, id: str, password: str):
    user = find_user(db, id)
    if user[0] is not None:
        if check_password(user[0], password)[0]:
            current_user['username'] = user[0]['username']
    return user


# print(table)
# print(register_user(database, 'Howard', 'superpass'))
# print(table)
# id_ = input('Enter id ')
# print(login(database, current_user, id_, 'superpass'))
# print(current_user)


def main():
    while True:
        command = input('Enter command ')
        if command == 'register':
            register_user(
                database,
                input('Enter username '),
                input('Enter password '),
                )
        elif command == 'db':
            print(table)
        elif command == 'login':
            login(
                database,
                current_user,
                input('Enter id '),
                input('Enter password '),
                )
            print(f'Welcome, {current_user["username"]}')
        elif command == 'stop':
            print('Goodbye')
            break


if __name__ == '__main__':
    main()


# TODO: logout
# TODO: написать crud для создания постов

# post = {
#     "id": ...,
#     "title": ...,
#     "author": ...,
#     "text": ...,
#     "created_at": ...,
# }
