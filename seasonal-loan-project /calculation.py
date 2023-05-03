# import necessary modules
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import math

# set loan interest rate
LOAN_INTEREST_RATE = 10.90


def calculate_loan_schedule(num_of_months, total_loan, periods_per_year, disbursement_date, due_date, loan_product, select_months):
    """
        calculates the repayment schedule for a loan.

        Args:
                - num_of_months: The number of months for the loan.
                - total_loan: The total amount of the loan.
                - periods_per_year: The number of periods (usually months) per year.
                - disbursement_date: The date the loan is disbursed.
                - due_date: The due date for the first repayment.
                - loan_product: The type of loan product.
                - select_months: The months for which to generate the repayment schedule.
        return: 
                - A list of dictionaries representing the repayment schedule, where each dictionary represents a single period.
    """

    # set processing fees
    processing_fees = 0.02

   # Initialize loan schedule and add processing fee as first item
    schedule = [
        {
            'period': "Fees",
            'date': disbursement_date,
            'interest': "-",
            'fees': "-",
            'principal': "-",
            'total_amount': processing_fees * total_loan,
        }
    ]

    # calculate the total number of payment periods
    payment_periods = (num_of_months / 12) * periods_per_year

    # calculate the initial payment amount
    total_amount = total_loan / payment_periods

    # set initial balance to the total_loan amount
    balance = total_loan

    # set the monthly due date to one month after disbursement date
    monthly_due_date = disbursement_date + relativedelta(months=1)

    # Initialize the accrued interest
    # and current_month paid variables
    accrued_interest = 0
    is_current_month_paid = False

    # calculate the total number of payment periods,
    # rounded up to the nearest integer
    all_payments_periods = math.ceil(num_of_months / 12) * periods_per_year

    # Calculate the monthly fees a
    # and the total fees to be paid over all payment periods
    Monthly_fees = 0.0035 * total_loan
    FEES = (Monthly_fees * num_of_months) / all_payments_periods

    # Loop through payment periods and add entries to the schedule
    for period in range(1, num_of_months + 1):

        # Calculate the number of days since the last payment
        if period == 1:
            monthly_due_date = monthly_due_date.replace(day=due_date)
            days_since_last_payment = (
                monthly_due_date - disbursement_date).days
        else:
            monthly_due_date = monthly_due_date + relativedelta(months=1)
            days_since_last_payment = (
                monthly_due_date - (monthly_due_date - relativedelta(months=1))).days

        # Get the current month
        current_month = monthly_due_date.strftime("%B")

        # interest due for this period
        interest = (balance * LOAN_INTEREST_RATE *
                    days_since_last_payment)/36000

        # Calculate principal due for the period
        principal = (total_amount - interest - FEES)

        # Check if current month is in the list of months selected
        if current_month in select_months:
            is_current_month_paid = True

            # Calculate principal and interest due for the current month.
            # TOTAL INTEREST IS C INT + ACCRUED
            interest = interest + accrued_interest
            principal = (total_amount - interest - FEES)

            # update balance for the next period
            balance -= principal

            # NULL THE ACCRUED INTEREST
            accrued_interest = 0

            # Add payment details to the schedule
            schedule.append({
                'period': period,
                'date': monthly_due_date,
                'interest': round(interest, 2),
                'fees': round(FEES, 2),
                'principal': round(principal, 2),
                'total_amount': round(total_amount, 2)
            })

        else:
            # Add interst to accrued_interest
            accrued_interest = interest + accrued_interest

            # Add an empty payment to the schedule for the current period
            schedule.append({
                'period': period,
                'date': monthly_due_date,
                'interest': "-",
                'fees': "-",
                'principal': "-",
                'total_amount': "-",
            })

    return schedule
