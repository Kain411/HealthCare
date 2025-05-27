from flask import Blueprint, jsonify, request
from controller import get_appointments_controller, get_appointment_by_id_controller, get_appointments_by_doctor_controller, get_appointment_details_by_patient_controller, post_new_appointment_controller, delete_apppointment_controller
import os
import requests
from dotenv import load_dotenv

load_dotenv()

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/', methods=['GET'])
def get_appointments_route():
    appointments = get_appointments_controller()

    if appointments!=[]:
        return jsonify({
            "appointments": appointments,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404
    
@appointment_bp.route('/<doctorID>', methods=['GET'])
def get_appointments_by_doctor_route(doctorID):
    doctor_url = os.getenv("DOCTOR_SERVICE")

    try:
        doctor_res = requests.get(f"{doctor_url}/{doctorID}")
        doctor_res.raise_for_status()
        doctor_data = doctor_res.json()
        if not doctor_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Doctor not found"
            }), 404
        
        appointments = get_appointments_by_doctor_controller(doctorID)

        if appointments!=[]:
            return jsonify({
                "doctor": doctor_data.get("doctor"),
                "appointments": appointments,
                "success": True,
                "message": "Success"
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Error: Not found appointment of doctor"
            }), 404

    except requests.exceptions.RequestException as e:
        return jsonify({
            "success": False,
            "error": "Error: Get doctor"
        }), 404
    
@appointment_bp.route('/patient/<patientID>', methods=['GET'])
def get_appointments_by_patient_route(patientID):
    patient_url = os.getenv("PATIENT_SERVICE")

    try:
        patient_res = requests.get(f"{patient_url}/{patientID}")
        patient_res.raise_for_status()
        patient_data = patient_res.json()
        if not patient_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Doctor not found"
            }), 404
        
        appointments = []
        appointmentDetails = get_appointment_details_by_patient_controller(patientID)
        for appointmentDetailData in appointmentDetails:
            appointment = get_appointment_by_id_controller(appointmentDetailData.get('appointmentID'))
            if appointment==None:
                return jsonify({
                    "success": False,
                    "error": "Error: Not found"
                }), 404
            appointments.append(appointment)

        if appointments!=[]:
            return jsonify({
                "patient": patient_data.get("patient"),
                "appointments": appointments,
                "success": True,
                "message": "Success"
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Error: Not found appointment of doctor"
            }), 404

    except requests.exceptions.RequestException as e:
        return jsonify({
            "success": False,
            "error": "Error: Get doctor"
        }), 404
    
@appointment_bp.route('/newAppointment', methods=['POST'])
def post_new_appointment_route():
    data = request.get_json()

    if post_new_appointment_controller(data):
        return jsonify({
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: Insert Error"
        }), 500

@appointment_bp.route('/deleteAppointment', methods=['DELETE'])
def delete_appointment_route():
    data = request.get_json()

    if delete_apppointment_controller(data):
        return jsonify({
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: Delete Error"
        }), 500