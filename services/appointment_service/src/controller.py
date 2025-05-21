from flask import current_app
from model import Appointment, AppointmentDetails
from bson import ObjectId

def get_appointments_controller():
    mongo = current_app.mongo
    appointmentRef = mongo.db.appointment.find()
    appointments = []
    for appointmentData in appointmentRef:
        appointment = Appointment.from_dict(appointmentData)
        appointments.append(appointment.to_dict())
    return appointments

def get_appointment_by_id_controller(id):
    mongo = current_app.mongo
    appointmentRef = mongo.db.appointment.find({"_id": ObjectId(id)})
    for appointmentData in appointmentRef:
        appointment = Appointment.from_dict(appointmentData)
        return appointment.to_dict()
    return None

def get_appointments_by_doctor_controller(doctorID):
    mongo = current_app.mongo
    appointmentRef = mongo.db.appointment.find({"doctorID": doctorID})
    appointments = []
    for appointmentData in appointmentRef:
        appointment = Appointment.from_dict(appointmentData)
        appointments.append(appointment.to_dict())
    return appointments

def get_appointment_details_by_patient_controller(patientID):
    mongo = current_app.mongo
    appointmentDetailRef = mongo.db.appointmentDetail.find({"patientID": patientID})
    appointmentDetails = []
    for appointmentDetailData in appointmentDetailRef:
        appointmentDetail = AppointmentDetails.from_dict(appointmentDetailData)
        appointmentDetails.append(appointmentDetail.to_dict())
    return appointmentDetails

def post_new_appointment_controller(data):
    mongo = current_app.mongo
    try: 
        result = mongo.db.appointmentDetail.insert_one(data)
        return True
    except Exception as e:
        return False