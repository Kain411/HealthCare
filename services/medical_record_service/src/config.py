import os
class Config:
    MONGO_URI = os.environ.get("MedicalRecordDB", "mongodb://host.docker.internal:27017/db_medical_record")