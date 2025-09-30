from flask import Flask, jsonify
from flask_cors import CORS
from models.database import db
from api.routes import api_bp
from config import Config
from flask_jwt_extended import JWTManager
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize JWT
jwt = JWTManager(app)

# Initialize database (only once, no retry logic needed)
db.init_app(app)

# Create tables within app context
with app.app_context():
    try:
        db.create_all()
        print("✓ Database tables created successfully")
    except Exception as e:
        print(f"⚠ Database initialization warning: {e}")
        # Don't fail - let Railway health check handle it

# Register API routes
app.register_blueprint(api_bp, url_prefix='/api/v1')

@app.route('/health')
def health():
    try:
        # Test database connection
        db.session.execute(db.text('SELECT 1'))
        db_status = 'connected'
    except Exception as e:
        db_status = f'error: {str(e)[:50]}'
    
    return jsonify({
        'status': 'healthy',
        'database': db_status,
        'port': os.getenv('PORT', '5000')
    })

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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
