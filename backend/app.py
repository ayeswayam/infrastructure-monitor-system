from flask import Flask, jsonify
from flask_cors import CORS
from models.database import db
from api.routes import api_bp
from config import Config
from flask_jwt_extended import JWTManager
import os
import time

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize JWT
jwt = JWTManager(app)

# Initialize database with retry logic
def init_database():
    max_retries = 5
    for i in range(max_retries):
        try:
            db.init_app(app)
            with app.app_context():
                db.create_all()
                print("Database connected successfully")
            return True
        except Exception as e:
            print(f"Database connection attempt {i+1} failed: {e}")
            if i < max_retries - 1:
                time.sleep(5)
    return False

# Initialize database
init_database()

# Register API routes
app.register_blueprint(api_bp, url_prefix='/api/v1')

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/')
def index():
    return jsonify({
        'name': 'AI Infrastructure Monitoring API',
        'status': 'running',
        'endpoints': {
            'health': '/health',
            'hosts': '/api/v1/hosts',
            'alerts': '/api/v1/alerts',
            'upload': '/api/v1/upload'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
