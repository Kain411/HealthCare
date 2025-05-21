from flask import Blueprint, jsonify, request
from controller import get_patients_controller, get_patient_by_id_controller, get_patient_by_username_controller, post_new_patient_controller, update_patient_by_id_controller

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/', methods=['GET'])
def get_patients_route():
    patients = get_patients_controller()

    if patients!=[]:
        return jsonify({
            "patients": patients,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404
    
@patient_bp.route('/<patientID>', methods=['GET'])
def get_patient_by_id_route(patientID):
    patient = get_patient_by_id_controller(patientID)

    if patient!=None:
        return jsonify({
            "patient": patient,
            "success": True,
            "message": "Success"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Error: No find patient"
        })

@patient_bp.route('/username/<patientName>', methods=['GET'])
def get_patient_by_username_route(patientName):
    patient = get_patient_by_username_controller(patientName)

    if patient!=None:
        return jsonify({
            "patient": patient,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No find user"
        }), 404

@patient_bp.route('/newPatient', methods=['POST'])
def post_new_patient_route():
    data = request.get_json()
    patient = post_new_patient_controller(data)

    if patient!=None:
        return jsonify({
            "patient": patient,
            "success": True,
            "message": "Register successful"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: Add new patient"
        }), 500
    
@patient_bp.route('/<patientID>/update', methods=['PUT'])
def update_patient_by_id_route(patientID):
    data = request.get_json()
    del data["id"]

    patient = update_patient_by_id_controller(patientID, data)
    if patient!=None:
        return jsonify({
            "patient": patient,
            "success": True,
            "message": "Update information successful"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: Update information"
        }), 500