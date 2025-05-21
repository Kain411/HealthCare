from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from route import doctor_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/doctors/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.config.from_object(Config)

mongo = PyMongo(app)
app.mongo = mongo

app.register_blueprint(doctor_bp, url_prefix='/doctors')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)