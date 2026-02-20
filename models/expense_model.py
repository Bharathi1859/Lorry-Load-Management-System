from datetime import datetime
from models.user_model import db


class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)

    load_id = db.Column(db.Integer, db.ForeignKey("loads.id"), nullable=False)

    category = db.Column(db.String(100), nullable=False)  
    # Example: Diesel, RTO, Toll, Maintenance

    amount = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    load = db.relationship("Load", backref=db.backref("expenses", lazy=True))

    def __repr__(self):
        return f"<Expense {self.category} - {self.amount}>"
