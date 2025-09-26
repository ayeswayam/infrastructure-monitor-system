from flask import Blueprint, jsonify
from models.anomaly import Anomaly
bp = Blueprint('analytics_v1', __name__)
@bp.route('/anomalies', methods=['GET'])
def get_anomalies():
    anomalies = Anomaly.query.order_by(Anomaly.detected_at.desc()).limit(100).all()
    return jsonify([a.to_dict() for a in anomalies])
@bp.route('/trends', methods=['GET'])
def get_trends():
    # sample synthetic trends
    return jsonify({'hosts_total':100,'unreachable':5,'falcon_issues':3})
@bp.route('/predictions', methods=['GET'])
def get_predictions():
    return jsonify({'predictions':[]})
