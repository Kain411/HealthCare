from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from route import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/users/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.config.from_object(Config)

mongo = PyMongo(app)
app.mongo = mongo

app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)