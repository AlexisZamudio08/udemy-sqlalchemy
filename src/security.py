from models.userModel import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.check_password(user.password, password):
        return user
    return None

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)