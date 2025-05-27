from flask import Flask, request, Response
import requests
from flask_cors import CORS  # Import flask_cors
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

SERVICE_MAP = {
    "users": os.getenv("USER_SERVICE"),
    "patients": os.getenv("PATIENT_SERVICE"),
    "doctors": os.getenv("DOCTOR_SERVICE"),
    "nurse": os.getenv("NURSE_SERVICE"),
    "appointments": os.getenv("APPOINTMENT_SERVICE"),
    "medical_records": os.getenv("MEDICAL_RECORD_SERVICE"),
    "prescriptions": os.getenv("PRESCRIPTION_SERVICE"),
    "medicines": os.getenv("MEDICINE_SERVICE"),
    "predicts": os.getenv("PREDICT_SERVICE"),
    "chats": os.getenv("CHAT_SERVICE")
}

@app.route("/<service>", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/<service>/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def proxy(service, path):
    if service not in SERVICE_MAP:
        return {"error": "Service not found"}, 404

    target_url = f"{SERVICE_MAP[service]}/{path}"
    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers={key: value for key, value in request.headers if key.lower() != "host"},
            params=request.args,
            data=request.get_data(),
            cookies=request.cookies,
        )
        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 502

@app.route("/")
def home():
    return {"message": "API Gateway is running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
