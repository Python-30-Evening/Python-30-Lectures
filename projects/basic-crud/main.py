# CRUD - Create Read Update Delete - 4 основные операции над объектами

# База данных - хранилище данных

database = []

commands = """
1. create
2. read all
3. read one
4. delete one
5. update one
6. stop
7. help
"""

while True:
    command = input('Enter command: ')
    if command == 'create':
        user = {
            'username': input('Enter username '),
            'password': input('Enter password '),
            'email': input('Enter email '),
        }
        database.append(user)
        print(database)
    elif command == 'read all':
        print(database)
    elif command == 'read one':
        username = input('Which one? ')
        for user in database:
            if user['username'] == username:
                print(user)
        else:
            print('Not found')
    elif command == 'delete one':
        username = input('Which one? ')
        for user in database:
            if user['username'] == username:
                database.remove(user)
                print(f"{user['username']} deleted")
        else:
            print('Not found')
    elif command == 'update one':
        username = input('Which one? ')
        for user in database:
            if user['username'] == username:
                database.remove(user)
                new_user = {
                    'username': input('Enter username ') or user['username'],
                    'password': input('Enter password ') or user['password'],
                    'email': input('Enter email ') or user['email'],
                }
                database.append(new_user)
        else:
            print('Not found')
    elif command == 'stop':
        print('Goobdye!')
        break
    elif command == 'help':
        print(commands)


# [{"user": 'kdshfgj', "password": 'superpassword', "email": "asdf@mail.com"}, {"user": 'asdfasdf', "password": 'superpassword', "email": "asdf@mail.com"}]

# TODO: добавить команду для остановки программы
# TODO: добавить команду для вывода списка команд
# DEADLINE: 5 минут
