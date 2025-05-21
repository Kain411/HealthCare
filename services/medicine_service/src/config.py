import os
class Config:
    MONGO_URI = os.environ.get("MedicineDB", "mongodb://host.docker.internal:27017/db_medicine")