from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from models.lorry_model import Lorry
from models.load_model import Load
from models.user_model import db
from datetime import datetime


lorry_bp = Blueprint("lorry", __name__)


@lorry_bp.route("/lorries")
@login_required
def lorries():

    lorries = Lorry.query.filter_by(user_id=current_user.id).all()
    return render_template("lorries.html", lorries=lorries)


@lorry_bp.route("/add_lorry", methods=["GET", "POST"])
@login_required
def add_lorry():

    if request.method == "POST":

        new_lorry = Lorry(
            vehicle_number=request.form.get("vehicle_number"),
            driver_name=request.form.get("driver_name"),
            driver_phone=request.form.get("driver_phone"),
            rc_expiry = datetime.strptime(request.form.get("rc_expiry"), "%Y-%m-%d").date(),
            insurance_expiry = datetime.strptime(request.form.get("insurance_expiry"), "%Y-%m-%d").date(),
            permit_expiry = datetime.strptime(request.form.get("permit_expiry"), "%Y-%m-%d").date(),
            status=request.form.get("status"),
            user_id=current_user.id
        )

        db.session.add(new_lorry)
        db.session.commit()

        return redirect(url_for("lorry.lorries"))

    return render_template("add_lorry.html")


@lorry_bp.route("/lorry/<int:lorry_id>")
@login_required
def lorry_details(lorry_id):

    lorry = Lorry.query.get_or_404(lorry_id)
    loads = Load.query.filter_by(lorry_id=lorry.id).all()

    total_revenue = sum(load.freight_amount for load in loads)
    total_expense = sum(load.total_expense for load in loads)
    total_profit = total_revenue - total_expense

    return render_template(
        "lorry_details.html",
        lorry=lorry,
        loads=loads,
        total_revenue=total_revenue,
        total_expense=total_expense,
        total_profit=total_profit
    )
