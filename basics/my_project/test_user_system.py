from main import register_user, login

test_database = []
test_current_user = {}


def test_register():
    register_user(test_database, 'testname', 'testpassword')
    assert test_database[0]['username'] == 'testname'


def test_login():
    register_user(test_database, 'testuser', 'testpass')
    success = login(test_database, test_current_user, 'testuser', 'testpass')
    wrong_username = login(test_database, test_current_user, 'wrong', 'testpass')
    wrong_password = login(test_database, test_current_user, 'testuser', 'wrong')
    assert success == 'Welcome, testuser'
    assert wrong_username == 'User not found'
    assert wrong_password == 'Invalid data'

