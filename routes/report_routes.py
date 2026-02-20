from flask import Blueprint, render_template, request
from flask_login import login_required
from models.load_model import Load
from models.user_model import db
from datetime import datetime

report_bp = Blueprint("report", __name__)


@report_bp.route("/reports")
@login_required
def reports():

    month = request.args.get("month", type=int) or datetime.now().month
    year = request.args.get("year", type=int) or datetime.now().year

    loads = Load.query.filter(
        db.extract('month', Load.date) == month,
        db.extract('year', Load.date) == year
    ).all()

    total_revenue = sum(load.freight_amount for load in loads)
    total_expense = sum(load.total_expense for load in loads)
    total_profit = total_revenue - total_expense

    return render_template(
        "reports.html",
        loads=loads,
        total_revenue=total_revenue,
        total_expense=total_expense,
        total_profit=total_profit,
        selected_month=month,
        selected_year=year
    )
