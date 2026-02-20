from datetime import datetime


def calculate_total_expense(load):
    """
    Calculate total expense for a single load
    """

    return (
        (load.diesel_amount or 0) +
        (load.rto_amount or 0) +
        (load.toll_amount or 0) +
        (load.driver_bata or 0) +
        (load.maintenance_amount or 0) +
        (load.other_expense or 0)
    )


def calculate_profit(load):
    """
    Calculate profit for a single load
    """

    total_expense = calculate_total_expense(load)
    return (load.freight_amount or 0) - total_expense


def calculate_lorry_summary(loads):
    """
    Calculate total revenue, expense, profit for a lorry
    """

    total_revenue = 0
    total_expense = 0

    for load in loads:
        total_revenue += load.freight_amount or 0
        total_expense += calculate_total_expense(load)

    total_profit = total_revenue - total_expense

    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "total_profit": total_profit
    }


def calculate_monthly_summary(loads, month=None, year=None):
    """
    Filter loads by month/year and calculate summary
    """

    if month and year:
        filtered_loads = [
            load for load in loads
            if load.date.month == month and load.date.year == year
        ]
    else:
        filtered_loads = loads

    return calculate_lorry_summary(filtered_loads)
