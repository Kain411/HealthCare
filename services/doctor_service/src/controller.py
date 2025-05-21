from flask import current_app
from model import Doctor
from bson import ObjectId

def get_doctors_controller():
    mongo = current_app.mongo
    doctorRef = mongo.db.doctor.find()
    doctors = []
    for doctorData in doctorRef:
        doctor = Doctor.from_dict(doctorData)
        doctors.append(doctor.to_dict())
    return doctors

def get_doctor_by_id_controller(id):
    mongo = current_app.mongo
    doctorRef = mongo.db.doctor.find({"_id": ObjectId(id)})

    for doctorData in doctorRef:
        doctor = Doctor.from_dict(doctorData)
        return doctor.to_dict()
    return None