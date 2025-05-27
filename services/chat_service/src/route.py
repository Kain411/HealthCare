from flask import Blueprint, jsonify, request
from controller import get_symptom_controller, get_diseases_controller

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/symptoms', methods=['GET'])
def get_symptom_route():
    symptoms = get_symptom_controller()

    if symptoms!=[]:
        return jsonify({
            "symptoms": symptoms,
            "success": True,
            "message": "Success"
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Error: No get symptoms"
        }), 404

@chat_bp.route('/predict', methods=['POST'])
def get_diseases_route():
    data = request.get_json()

    result = get_diseases_controller(data.get('symptoms'))

    
    if len(result)==0:
        return jsonify({
            "success": True,
            "message": "Không chẩn đoán được bệnh"
        }), 200
    elif len(result)==1:
        return jsonify({
            "specialty": result[0].get('specialty'),
            "success": True,
            "message": "Kết quả: " + str(result[0].get('name'))
        }), 200
    else:
        message = "Bạn có thể mắc các bệnh sau:" + '\n'
        for doc in result:
            message += doc.get('name') + '\n'
        return jsonify({
            "success": True,
            "message": message
        }), 200