import os
class Config:
    MONGO_URI = os.environ.get("UserDB", "mongodb://host.docker.internal:27017/db_user")