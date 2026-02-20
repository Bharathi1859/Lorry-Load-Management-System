from datetime import datetime


def format_date(date_obj):
    """
    Convert date to readable format
    Example: 18-02-2026
    """

    if not date_obj:
        return ""

    return date_obj.strftime("%d-%m-%Y")


def format_currency(amount):
    """
    Format currency with 2 decimals
    """

    try:
        return f"₹ {float(amount):,.2f}"
    except (TypeError, ValueError):
        return "₹ 0.00"


def safe_float(value):
    """
    Safely convert form input to float
    """

    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def lorry_status_badge(status):
    """
    Return bootstrap badge class based on status
    """

    status = (status or "").lower()

    if status == "active":
        return "success"
    elif status == "maintenance":
        return "warning"
    elif status == "inactive":
        return "danger"
    else:
        return "secondary"
