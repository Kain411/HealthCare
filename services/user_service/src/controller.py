from flask import current_app
from model import User
from bson import ObjectId

def register_controller(data):
    mongo = current_app.mongo
    try:
        result = mongo.db.user.insert_one(data)
        id = str(result.inserted_id)

        return True
    except Exception as e:
        return False
    
def login_controller(data):
    mongo = current_app.mongo
    user = mongo.db.user.find_one({
        "username": data.get("username"),
        "password": data.get("password"),
        "role": data.get("role")
    })

    return user is not None