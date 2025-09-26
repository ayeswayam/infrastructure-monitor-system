from .database import db
from datetime import datetime
class Host(db.Model):
    __tablename__='hosts'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), unique=True, nullable=False)
    ip_address = db.Column(db.String(50), nullable=False)
    os_distribution = db.Column(db.String(50))
    falcon_status = db.Column(db.String(20), default='Unknown')
    falcon_version = db.Column(db.String(20))
    is_reachable = db.Column(db.Boolean, default=True)
    owner_name = db.Column(db.String(100))
    owner_email = db.Column(db.String(100))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
