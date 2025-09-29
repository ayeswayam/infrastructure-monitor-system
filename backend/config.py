import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Fix Railway's DATABASE_URL format
    db_url = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost/db')
    if db_url.startswith('postgres://'):
        db_url = db_url.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Use Railway's PORT or default
    PORT = os.getenv('PORT', 5000)
    
    # Security
    JWT_SECRET_KEY = os.getenv('JWT_SECRET', 'dev-secret-key')
    SECRET_KEY = JWT_SECRET_KEY
