from flask import Blueprint, jsonify, request
from controller import register_controller, login_controller
import os
import requests
from dotenv import load_dotenv

load_dotenv()

user_bp = Blueprint('user', __name__)

patient_url = os.getenv("PATIENT_SERVICE")
doctor_url = os.getenv("DOCTOR_SERVICE")

@user_bp.route('/register', methods=['POST'])
def register_route():
    data = request.get_json()

    if not register_controller(data):
        return jsonify({
            "success": False,
            "error": "Error: Register failed"
        }), 500

    if data.get('role')=="Patient":
        tmp = {
            "username": data.get('username'),
            "gender": "",
            "insuranceNumber": "",
            "bloodType": "",
            "phone": "",
            "location": ""
        }
        patient_res = requests.post(f"{patient_url}/newPatient", json=tmp)
        patient_res.raise_for_status()
        patient_data = patient_res.json()

        if patient_data.get('success'):
            return jsonify({
                "patient": patient_data.get('patient'),
                "success": True,
                "message": patient_data.get('message')
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Error: Add new patient"
            }), 500
    else: 
        return jsonify({
            "success": True
        })
    
@user_bp.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()

    if not login_controller(data):
        return jsonify({
            "success": False,
            "error": "Error: Login failed"
        }), 500
    
    if data.get('role')=="Patient":
        patient_res = requests.get(f"{patient_url}/username/{data.get('username')}")
        patient_res.raise_for_status()
        patient_data = patient_res.json()

        if patient_data.get('success'):
            return jsonify({
                "patient": patient_data.get('patient'),
                "success": True,
                "message": patient_data.get('message')
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Error: Add new patient"
            }), 500
    else: 
        return jsonify({
            "success": True
        })