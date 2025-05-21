from flask import current_app
from model import MedicalRecord
from bson import ObjectId

def get_medical_records_controller():
    mongo = current_app.mongo
    medicalRecordRef = mongo.db.medicalRecord.find()
    medical_records = []
    for medicalRecordData in medicalRecordRef:
        medical_record = MedicalRecord.from_dict(medicalRecordData)
        medical_records.append(medical_record.to_dict())
    return medical_records

def get_medical_record_by_patient_controller(patientID):
    mongo = current_app.mongo
    medicalRecordRef = mongo.db.medicalRecord.find({"patientID": patientID})
    medical_records = []
    for medicalRecordData in medicalRecordRef:
        medical_record = MedicalRecord.from_dict(medicalRecordData)
        medical_records.append(medical_record.to_dict())
    return medical_records