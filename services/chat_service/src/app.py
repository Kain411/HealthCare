from flask import Flask
from route import chat_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/chats/*": {"origins": "http://localhost:3000", "supports_credentials": True}})

app.register_blueprint(chat_bp, url_prefix='/chats')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)