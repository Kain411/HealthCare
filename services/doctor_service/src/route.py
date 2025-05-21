from flask import Blueprint, jsonify
from controller import get_doctors_controller, get_doctor_by_id_controller

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/', methods=['GET'])
def get_doctors_route():
    doctors = get_doctors_controller()

    if doctors!=[]:
        return jsonify({
            "doctors": doctors,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404
    
@doctor_bp.route('/<doctorID>', methods=['GET'])
def get_doctor_by_id_route(doctorID):
    doctor = get_doctor_by_id_controller(doctorID)

    if doctor!=None:
        return jsonify({
            "doctor": doctor,
            "success": True,
            "message": "Success"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Error: No find doctor"
        })