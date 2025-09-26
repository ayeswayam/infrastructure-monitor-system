from flask import Flask, jsonify
from flask_cors import CORS
from models.database import db, init_db
from api.routes import api_bp
from config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, static_folder='../frontend', static_url_path='/')
    app.config.from_object(Config)
    CORS(app)
    jwt = JWTManager(app)
    init_db(app)
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    @app.route('/health')
    def health():
        return jsonify({'status':'ok'})
    # serve frontend index
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
