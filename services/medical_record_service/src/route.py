from flask import Blueprint, jsonify
from controller import get_medical_records_controller, get_medical_record_by_patient_controller
import os
import requests
from dotenv import load_dotenv

load_dotenv()

medical_record_bp = Blueprint('medical_record', __name__)

@medical_record_bp.route('/', methods=['GET'])
def get_medical_records_route():
    patient_url = os.getenv("PATIENT_SERVICE")
    doctor_url = os.getenv("DOCTOR_SERVICE")
    nurse_url = os.getenv("NURSE_SERVICE")

    res = []
    medical_records = get_medical_records_controller()
    for medical_record in medical_records:
        patient_res = requests.get(f"{patient_url}/{medical_record.get('patientID')}")
        patient_res.raise_for_status()
        patient_data = patient_res.json()
        if not patient_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Patient not found"
            }), 404
        
        doctor_res = requests.get(f"{doctor_url}/{medical_record.get('doctorID')}")
        doctor_res.raise_for_status()
        doctor_data = doctor_res.json()
        if not doctor_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Doctor not found"
            }), 404
        
        nurse_res = requests.get(f"{nurse_url}/{medical_record.get('nurseID')}")
        nurse_res.raise_for_status()
        nurse_data = nurse_res.json()
        if not nurse_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Nurse not found"
            }), 404
        
        tmp = {
            "patient": patient_data.get('patient'),
            "doctor": doctor_data.get('doctor'),
            "nurse": nurse_data.get('nurse'),
            "note": medical_record.get('note'),
            "result": medical_record.get('result')
        }
        res.append(tmp)

    if medical_records!=[]:
        return jsonify({
            "medical_records": res,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404
    
@medical_record_bp.route('/<patientID>', methods=['GET'])
def get_medical_record_by_patient_route(patientID):
    patient_url = os.getenv("PATIENT_SERVICE")
    doctor_url = os.getenv("DOCTOR_SERVICE")
    nurse_url = os.getenv("NURSE_SERVICE")

    try:
        patient_res = requests.get(f"{patient_url}/{patientID}")
        patient_res.raise_for_status()
        patient_data = patient_res.json()
        if not patient_data.get("success"):
            return jsonify({
                "success": False,
                "error": "Error: Patient not found"
            }), 404
        
        res = []
        medical_records = get_medical_record_by_patient_controller(patientID)
        for medical_record in medical_records:
            doctor_res = requests.get(f"{doctor_url}/{medical_record.get('doctorID')}")
            doctor_res.raise_for_status()
            doctor_data = doctor_res.json()
            if not doctor_data.get("success"):
                return jsonify({
                    "success": False,
                    "error": "Error: Doctor not found"
                }), 404
            
            nurse_res = requests.get(f"{nurse_url}/{medical_record.get('nurseID')}")
            nurse_res.raise_for_status()
            nurse_data = nurse_res.json()
            if not nurse_data.get("success"):
                return jsonify({
                    "success": False,
                    "error": "Error: Nurse not found"
                }), 404
            
            tmp = {
                "doctor": doctor_data.get('doctor'),
                "nurse": nurse_data.get('nurse'),
                "note": medical_record.get('note'),
                "result": medical_record.get('result')
            }
            res.append(tmp)

        if medical_records!=[]:
            return jsonify({
                "patient": patient_data.get('patient'),
                "medical_records": res,
                "success": True,
                "message": "Success"
            }), 200
        else:
            return jsonify({
                "success": False,
                "error": "Error: No data"
            }), 404

    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Error: Get doctor"
        }), 404