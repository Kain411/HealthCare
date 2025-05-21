from flask import Blueprint, jsonify, request
from controller import get_medicines_controller, get_medicine_by_id_controller

medicine_bp = Blueprint('medicine', __name__)

@medicine_bp.route('/', methods=['GET'])
def get_medicines_route():
    medicines = get_medicines_controller()

    if medicines!=[]:
        return jsonify({
            "medicines": medicines,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404

@medicine_bp.route('/<medicineID>', methods=['GET'])
def get_medicine_by_id_route(medicineID):
    medicine = get_medicine_by_id_controller(medicineID)

    if medicine!=None:
        return jsonify({
            "medicine": medicine,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({ 
            "success": False,
            "error": "Error: No found"
        }), 404