from .database import db
from datetime import datetime
class Anomaly(db.Model):
    __tablename__='anomalies'
    id = db.Column(db.Integer, primary_key=True)
    host_id = db.Column(db.Integer, db.ForeignKey('hosts.id'), nullable=True)
    anomaly_score = db.Column(db.Float)
    anomaly_type = db.Column(db.String(50))
    features = db.Column(db.JSON)
    detected_at = db.Column(db.DateTime, default=datetime.utcnow)
    def to_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}
