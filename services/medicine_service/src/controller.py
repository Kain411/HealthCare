from flask import current_app
from model import Medicine
from bson import ObjectId

def get_medicines_controller():
    mongo = current_app.mongo
    medicineRef = mongo.db.medicine.find()
    medicines = []
    for medicineData in medicineRef:
        medicine = Medicine.from_dict(medicineData)
        medicines.append(medicine.to_dict())
    return medicines

def get_medicine_by_id_controller(id):
    mongo = current_app.mongo
    medicineRef = mongo.db.medicine.find({"_id": ObjectId(id)})

    for medicineData in medicineRef:
        medicine = Medicine.from_dict(medicineData)
        return medicine.to_dict()
    return None