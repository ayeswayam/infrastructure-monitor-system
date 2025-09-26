from flask import Blueprint, request, jsonify
import pandas as pd
from models.host import Host
from models.database import db
bp = Blueprint('upload_v1', __name__)
@bp.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'no file'}),400
    f = request.files['file']
    if f.filename.endswith('.csv'):
        df = pd.read_csv(f)
    else:
        df = pd.read_excel(f)
    required = ['hostname','ip_address','os_distribution','falcon_status','owner_name']
    missing = [c for c in required if c not in df.columns]
    if missing:
        return jsonify({'error':'missing columns','missing':missing}),400
    inserted = 0
    for _,row in df.fillna('').iterrows():
        if not row.get('hostname') or not row.get('ip_address'):
            continue
        h = Host(
            hostname=str(row['hostname']),
            ip_address=str(row['ip_address']),
            os_distribution=str(row.get('os_distribution','')),
            falcon_status=str(row.get('falcon_status','Unknown')),
            owner_name=str(row.get('owner_name','')),
            owner_email=str(row.get('owner_email',''))
        )
        db.session.add(h); inserted+=1
    db.session.commit()
    return jsonify({'inserted':inserted}),200
