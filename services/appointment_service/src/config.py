import os
class Config:
    MONGO_URI = os.environ.get("AppointmentDB", "mongodb://host.docker.internal:27017/db_appointment")