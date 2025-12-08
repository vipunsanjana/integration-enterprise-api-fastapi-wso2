from app.db.fake_db import users_db

def create_user(user):
    user_dict = user.dict()
    user_dict["id"] = len(users_db) + 1
    users_db.append(user_dict)
    return user_dict

def get_users():
    return users_db
