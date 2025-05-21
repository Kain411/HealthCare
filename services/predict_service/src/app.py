from flask import Flask
from route import predict_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predicts/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.register_blueprint(predict_bp, url_prefix='/predicts')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)