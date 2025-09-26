from .database import db
from datetime import datetime
class Alert(db.Model):
    __tablename__='alerts'
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=True)
    alert_type = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    message = db.Column(db.Text)
    status = db.Column(db.String(20), default='open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    acknowledged_at = db.Column(db.DateTime, nullable=True)
    resolved_at = db.Column(db.DateTime, nullable=True)
    def to_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}
