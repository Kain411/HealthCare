from flask import Blueprint, jsonify
from controller import get_prescriptions_by_patient_controller, get_prescription_details_controller
import os
import requests
from dotenv import load_dotenv

load_dotenv()

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/<patientID>', methods=['GET'])
def get_prescriptions_by_patient_route(patientID):
    patient_url = os.getenv("PATIENT_SERVICE")
    doctor_url = os.getenv("DOCTOR_SERVICE")
    medicine_url = os.getenv("MEDICINE_SERVICE")

    try:
        patient_res = requests.get(f"{patient_url}/{patientID}")
        patient_res.raise_for_status()
        patient_data = patient_res.json()
        if not patient_data.get("success"):
            return jsonify({"success": False, "error": "Patient not found"}), 404
        patient = patient_data.get("patient")
    except requests.exceptions.RequestException as e:
        return jsonify({"success": False, "error": f"Patient service error: {str(e)}"}), 502

    prescriptions = get_prescriptions_by_patient_controller(patientID)
    if not prescriptions:
        return jsonify({"success": False, "error": "No prescriptions found"}), 404

    result = []

    for prescription in prescriptions:
        try:
            doctor_res = requests.get(f"{doctor_url}/{prescription['doctorID']}")
            doctor_res.raise_for_status()
            doctor_data = doctor_res.json()
            if not doctor_data.get("success"):
                return jsonify({"success": False, "error": "Doctor not found"}), 404
            doctor = doctor_data.get("doctor")
        except requests.exceptions.RequestException as e:
            return jsonify({"success": False, "error": f"Doctor service error: {str(e)}"}), 502

        prescriptionDetails = get_prescription_details_controller(prescription["id"])
        if not prescriptionDetails:
            return jsonify({"success": False, "error": "No prescription details found"}), 404

        details = []
        for detail in prescriptionDetails:
            try:
                medicine_res = requests.get(f"{medicine_url}/{detail['medicineID']}")
                medicine_res.raise_for_status()
                medicine_data = medicine_res.json()
                if not medicine_data.get("success"):
                    return jsonify({"success": False, "error": "Medicine not found"}), 404
                medicine = medicine_data.get("medicine")
            except requests.exceptions.RequestException as e:
                return jsonify({"success": False, "error": f"Medicine service error: {str(e)}"}), 502

            details.append({
                "id": detail["id"],
                "prescriptionID": detail["prescriptionID"],
                "quantity": detail["quantity"],
                "medicine": medicine
            })

        result.append({
            "id": prescription["id"],
            "patient": patient,
            "doctor": doctor,
            "prescriptionDetails": details
        })

    return jsonify({
        "success": True,
        "message": "Success",
        "prescriptions": result
    }), 200
