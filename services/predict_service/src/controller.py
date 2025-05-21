from model import Predict

def predict_controller(data):
    predict = Predict(
        data.get('age'),
        data.get('gender'),
        data.get('fever'),
        data.get('chestPain'),
        data.get('breath'),
        data.get('cough'),
        data.get('dizzy'),
        data.get('bloodPressure'),
        data.get('heartRate')
    )

    return predict.getData()