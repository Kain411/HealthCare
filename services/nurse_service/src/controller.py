from flask import current_app
from model import Nurse
from bson import ObjectId

def get_nurses_controller():
    mongo = current_app.mongo
    nurseRef = mongo.db.nurse.find()
    nurses = []
    for nurseData in nurseRef:
        nurse = Nurse.from_dict(nurseData)
        nurses.append(nurse.to_dict())
    return nurses

def get_nurse_by_id_controller(id):
    mongo = current_app.mongo
    nurseRef = mongo.db.nurse.find({"_id": ObjectId(id)})

    for nurseData in nurseRef:
        nurse = Nurse.from_dict(nurseData)
        return nurse.to_dict()
    return None