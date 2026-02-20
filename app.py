from flask import Flask, render_template
from flask_login import LoginManager
from config import config_by_name
from models.user_model import db, User
from routes.auth_routes import auth
from routes.lorry_routes import lorry_bp
from routes.load_routes import load_bp
from routes.report_routes import report_bp
from models.load_model import Load 
import os


def create_app():

    app = Flask(__name__)

    # Load configuration
    env = os.environ.get("FLASK_ENV") or "development"
    app.config.from_object(config_by_name[env])

    # Initialize Database
    db.init_app(app)

    # Setup Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(lorry_bp)
    app.register_blueprint(load_bp)
    app.register_blueprint(report_bp)

    # Dashboard Route
    from collections import defaultdict
    from flask_login import login_required

    from collections import defaultdict
    from datetime import datetime

    @app.route("/")
    @login_required
    def dashboard():

        loads = Load.query.all()

        total_revenue = sum(load.freight_amount or 0 for load in loads)
        total_expense = sum(load.total_expense or 0 for load in loads)
        total_profit = total_revenue - total_expense

        total_due = 0  # You can implement later if needed

        # Recent loads
        recent_loads = Load.query.order_by(Load.date.desc()).limit(5).all()

        # Monthly chart data
        monthly_data = defaultdict(lambda: {"revenue": 0, "expense": 0})

        for load in loads:
            if load.date:
                key = load.date.strftime("%b %Y")
                monthly_data[key]["revenue"] += load.freight_amount or 0
                monthly_data[key]["expense"] += load.total_expense or 0

        chart_labels = list(monthly_data.keys())
        chart_revenue = [v["revenue"] for v in monthly_data.values()]
        chart_expense = [v["expense"] for v in monthly_data.values()]

        return render_template(
            "dashboard.html",
            total_revenue=total_revenue,
            total_expense=total_expense,
            total_profit=total_profit,
            total_due=total_due,
            recent_loads=recent_loads,
            chart_labels=chart_labels,
            chart_revenue=chart_revenue,
            chart_expense=chart_expense
        )

    return app


# Run App
if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(debug=True)
