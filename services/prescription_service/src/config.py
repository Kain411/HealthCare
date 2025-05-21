import os
class Config:
    MONGO_URI = os.environ.get("PrescriptionDB", "mongodb://host.docker.internal:27017/db_prescription")