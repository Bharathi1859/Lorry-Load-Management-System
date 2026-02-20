from datetime import datetime
from models.user_model import db


class Lorry(db.Model):
    __tablename__ = "lorries"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_number = db.Column(db.String(50), unique=True, nullable=False)
    driver_name = db.Column(db.String(100), nullable=False)
    driver_phone = db.Column(db.String(20), nullable=False)

    rc_expiry = db.Column(db.Date)
    insurance_expiry = db.Column(db.Date)
    permit_expiry = db.Column(db.Date)

    status = db.Column(db.String(20), default="active")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Relationship
    loads = db.relationship("Load", backref="lorry", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Lorry {self.vehicle_number}>"
