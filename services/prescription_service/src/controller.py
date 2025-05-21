from flask import current_app
from model import Prescription, PrescriptionDetails

def get_prescriptions_by_patient_controller(patientID):
    mongo = current_app.mongo
    prescriptionRef = mongo.db.prescription.find({"patientID": patientID})
    prescriptions = []
    for prescriptionData in prescriptionRef:
        prescription = Prescription.from_dict(prescriptionData)
        prescriptions.append(prescription.to_dict())
    return prescriptions

def get_prescription_details_controller(prescriptionID):
    mongo = current_app.mongo
    prescriptionDetailRef = mongo.db.prescriptionDetail.find({"prescriptionID": prescriptionID})
    prescriptionDetails = []
    for prescriptionDetailData in prescriptionDetailRef:
        prescriptionDetail = PrescriptionDetails.from_dict(prescriptionDetailData)
        prescriptionDetails.append(prescriptionDetail.to_dict())
    return prescriptionDetails
            