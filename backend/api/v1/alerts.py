from flask import Blueprint, request, jsonify
from models.alert import Alert
from models.database import db
bp = Blueprint('alerts_v1', __name__)
@bp.route('/', methods=['GET'])
def list_alerts():
    alerts = Alert.query.order_by(Alert.created_at.desc()).all()
    return jsonify([a.to_dict() for a in alerts])
@bp.route('/', methods=['POST'])
def create_alert():
    data = request.json
    a = Alert(
        host_id=data.get('host_id'),
        alert_type=data.get('alert_type','generic'),
        severity=data.get('severity','medium'),
        message=data.get('message','')
    )
    db.session.add(a); db.session.commit()
    return jsonify(a.to_dict()),201
@bp.route('/<int:id>', methods=['PUT'])
def update_alert(id):
    a = Alert.query.get_or_404(id)
    data = request.json
    for k,v in data.items():
        if hasattr(a,k):
            setattr(a,k,v)
    db.session.commit()
    return jsonify(a.to_dict())
