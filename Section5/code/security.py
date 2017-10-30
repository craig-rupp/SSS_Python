from werkzeug.security import safe_str_cmp
from user import User
users = [
    User(1, 'Bob', 'Burgers')
]
username_mapping = {
    # 'Bob' : {
    #     'id' : 1,
    #     'username' : 'Bob',
    #     'password' : 'Burgers'
    # }
    u.username: u for u in users
}

user_id_mapping = {
    # 1 : {
    #     'id' : 1,
    #     'username' : 'Bob',
    #     'password' : 'Burgers'
    # }
    u.id: u for u in users
}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    # .get method can be called of dictionary and is passed key and , None if not found
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)