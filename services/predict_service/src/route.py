from flask import Blueprint, jsonify, request
from main import Main
from controller import predict_controller

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/', methods=['POST'])
def predict_route():
    data = request.get_json()

    main = Main()
    lst = main.main()
    predictLst = predict_controller(data)

    result_text = "Không phân loại được bệnh"
    for i in lst:
        ok = True
        for key in i.keys():
            if key!="Bệnh":
                if i[key]!=predictLst[key]:
                    ok = False
                    break
        if ok: 
            result_text = "Bệnh: " + i["Bệnh"]
            break

    return jsonify({
        "predict": result_text
    })