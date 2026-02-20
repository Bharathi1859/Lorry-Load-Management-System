from datetime import datetime
from models.user_model import db


class Load(db.Model):
    __tablename__ = "loads"

    id = db.Column(db.Integer, primary_key=True)

    lorry_id = db.Column(db.Integer, db.ForeignKey("lorries.id"), nullable=False)

    date = db.Column(db.Date, nullable=False)
    from_location = db.Column(db.String(150), nullable=False)
    to_location = db.Column(db.String(150), nullable=False)

    freight_amount = db.Column(db.Float, nullable=False)

    diesel_amount = db.Column(db.Float, default=0)
    rto_amount = db.Column(db.Float, default=0)
    toll_amount = db.Column(db.Float, default=0)
    driver_bata = db.Column(db.Float, default=0)
    maintenance_amount = db.Column(db.Float, default=0)
    other_expense = db.Column(db.Float, default=0)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ---------- Calculated Properties ----------

    @property
    def total_expense(self):
        return (
            (self.diesel_amount or 0) +
            (self.rto_amount or 0) +
            (self.toll_amount or 0) +
            (self.driver_bata or 0) +
            (self.maintenance_amount or 0) +
            (self.other_expense or 0)
        )

    @property
    def profit(self):
        return (self.freight_amount or 0) - self.total_expense

    def __repr__(self):
        return f"<Load {self.id}>"
