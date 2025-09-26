from flask import Blueprint
from .v1 import hosts, upload, alerts, analytics, websocket
api_bp = Blueprint('api', __name__)
# register v1 blueprints
api_bp.register_blueprint(hosts.bp, url_prefix='/hosts')
api_bp.register_blueprint(alerts.bp, url_prefix='/alerts')
api_bp.register_blueprint(upload.bp, url_prefix='/upload')
api_bp.register_blueprint(analytics.bp, url_prefix='/analytics')
