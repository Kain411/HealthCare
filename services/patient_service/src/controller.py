from flask import current_app
from model import Patient
from bson import ObjectId

def get_patients_controller():
    mongo = current_app.mongo
    patientRef = mongo.db.patient.find()
    patients = []
    for patientData in patientRef:
        patient = Patient.from_dict(patientData)
        patients.append(patient.to_dict())
    return patients

def get_patient_by_id_controller(id):
    mongo = current_app.mongo
    patientRef = mongo.db.patient.find({"_id": ObjectId(id)})

    for patientData in patientRef:
        patient = Patient.from_dict(patientData)
        return patient.to_dict()
    return None

def get_patient_by_username_controller(username):
    mongo = current_app.mongo
    patientRef = mongo.db.patient.find({"username": username})
    
    for patientData in patientRef:
        patient = Patient.from_dict(patientData)
        return patient.to_dict()
    return None

def post_new_patient_controller(data):
    mongo = current_app.mongo
    try:
        result = mongo.db.patient.insert_one(data)
        id = str(result.inserted_id)
        data["id"] = id

        patient = Patient.from_dict(data)
        return patient.to_dict()
    except Exception as e:
        return None
    
def update_patient_by_id_controller(id, data):
    mongo = current_app.mongo
    try:
        mongo.db.patient.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
        )
        data["id"] = id
        patient = Patient.from_dict(data)
        return patient.to_dict()
    except Exception as e:
        return None