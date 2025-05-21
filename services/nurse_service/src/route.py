from flask import Blueprint, jsonify
from controller import get_nurses_controller, get_nurse_by_id_controller

nurse_bp = Blueprint('nurse', __name__)

@nurse_bp.route('/', methods=['GET'])
def get_nurses_route():
    nurses = get_nurses_controller()

    if nurses!=[]:
        return jsonify({
            "nurses": nurses,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "error": "Error: No data"
        }), 404
    
@nurse_bp.route('/<nurseID>', methods=['GET'])
def get_nurse_by_id_route(nurseID):
    nurse = get_nurse_by_id_controller(nurseID)

    if nurse!=None:
        return jsonify({
            "nurse": nurse,
            "success": True,
            "message": "Success"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Error: No find nurse"
        })