from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.load_model import Load
from models.lorry_model import Lorry
from models.user_model import db
from datetime import datetime


load_bp = Blueprint("load", __name__)



@load_bp.route("/add_load", methods=["GET", "POST"])
@login_required
def add_load():

    lorries = Lorry.query.all()

    if request.method == "POST":

        new_load = Load(
            lorry_id=request.form.get("lorry_id"),
            date=datetime.strptime(request.form.get("date"), "%Y-%m-%d").date(),
            from_location=request.form.get("from_location"),
            to_location=request.form.get("to_location"),
            freight_amount=float(request.form.get("freight_amount")),
            diesel_amount=float(request.form.get("diesel_amount")),
            rto_amount=float(request.form.get("rto_amount")),
            toll_amount=float(request.form.get("toll_amount")),
            driver_bata=float(request.form.get("driver_bata")),
            maintenance_amount=float(request.form.get("maintenance_amount")),
            other_expense=float(request.form.get("other_expense"))
        )

        db.session.add(new_load)
        db.session.commit()

        return redirect(url_for("load.loads"))

    return render_template("add_load.html", lorries=lorries)

@load_bp.route("/edit/<int:load_id>", methods=["GET", "POST"])
@login_required
def edit_load(load_id):
    load = Load.query.get_or_404(load_id)

    if request.method == "POST":
        load.from_location = request.form.get("from_location")
        load.to_location = request.form.get("to_location")
        load.freight_amount = float(request.form.get("freight_amount"))

        db.session.commit()
        return redirect(url_for("load.loads"))

    return render_template("edit_load.html", load=load)

from sqlalchemy import func

@load_bp.route("/loads")
@login_required
def loads():

    loads = Load.query.all()

    # Group by lorry and calculate totals
    lorry_summary = db.session.query(
        Lorry.id,
        Lorry.vehicle_number,
        func.sum(Load.freight_amount).label("total_revenue"),
        func.sum(Load.total_expense).label("total_expense"),
        func.sum(Load.profit).label("total_profit")
    ).join(Load).group_by(Lorry.id).all()

    return render_template(
        "loads.html",
        loads=loads,
        lorry_summary=lorry_summary
    )


