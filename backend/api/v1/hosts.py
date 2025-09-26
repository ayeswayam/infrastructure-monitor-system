from flask import Blueprint, request, jsonify
from models.host import Host
from models.database import db
bp = Blueprint('hosts_v1', __name__)
@bp.route('/', methods=['GET'])
def list_hosts():
    hosts = Host.query.all()
    return jsonify([h.to_dict() for h in hosts])
@bp.route('/', methods=['POST'])
def create_host():
    data = request.json
    h = Host(
        hostname=data['hostname'],
        ip_address=data['ip_address'],
        os_distribution=data.get('os_distribution'),
        falcon_status=data.get('falcon_status','Unknown'),
        owner_name=data.get('owner_name'),
        owner_email=data.get('owner_email')
    )
    db.session.add(h); db.session.commit()
    return jsonify(h.to_dict()), 201
@bp.route('/<int:id>', methods=['GET'])
def get_host(id):
    h = Host.query.get_or_404(id)
    return jsonify(h.to_dict())
@bp.route('/<int:id>', methods=['PUT'])
def update_host(id):
    h = Host.query.get_or_404(id)
    data = request.json
    for k,v in data.items():
        if hasattr(h,k):
            setattr(h,k,v)
    db.session.commit()
    return jsonify(h.to_dict())
@bp.route('/<int:id>', methods=['DELETE'])
def delete_host(id):
    h = Host.query.get_or_404(id)
    db.session.delete(h); db.session.commit()
    return '',204
