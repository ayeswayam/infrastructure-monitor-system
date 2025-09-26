import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://monitor:monitorpass@db:5432/monitor_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET','change-me-please')
    SECRET_KEY = JWT_SECRET_KEY
