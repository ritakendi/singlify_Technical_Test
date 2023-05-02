from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import math

LOAN_INTEREST_RATE = 10.90


def calculate_loan_schedule(num_of_months, total_loan, periods_per_year, disbursement_date, due_date, loan_product, select_months):
    processing_fees = 0.02
    # initialize loan schedule
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

    # total payment period
    payment_periods = (num_of_months / 12) * periods_per_year
    # pmt initial
    total_amount = total_loan / payment_periods
    # print(total_amount)

    # set initial balance to the total amount
    balance = total_loan

    prev_due_date = disbursement_date

    monthly_due_date = disbursement_date + relativedelta(months=1)

    accrued_interest = 0
    is_current_month_paid = False

    all_payments_periods = math.ceil(num_of_months / 12) * periods_per_year
    Monthly_fees = 0.0035 * total_loan
    FEES = (Monthly_fees * num_of_months) / all_payments_periods
    print(FEES)

    # loop through payment periods and add entries to the schedule
    for period in range(1, num_of_months + 1):
        # number of days since the last payment

        if period == 1:

            monthly_due_date = monthly_due_date.replace(day=due_date)
            days_since_last_payment = (
                monthly_due_date - disbursement_date).days
        else:
            monthly_due_date = monthly_due_date + relativedelta(months=1)
            days_since_last_payment = (
                monthly_due_date - (monthly_due_date - relativedelta(months=1))).days

        current_month = monthly_due_date.strftime("%B")

        # interest due for this period
        interest = (balance * LOAN_INTEREST_RATE *
                    days_since_last_payment)/36000

        # principal due for the period
        principal = (total_amount - interest - FEES)

        # add payment to the schedule
        # schedule.append(payment)

        # print(f"Interest: ", interest, "Balance: ", balance)
        # print(f"days_since_last_payment, {days_since_last_payment}")

        if current_month in select_months:
            is_current_month_paid = True
            # Calculate principal, interest etc

            # TOTAL INTEREST IS C INT + ACCRUED
            interest = interest + accrued_interest

            principal = (total_amount - interest - FEES)
            # update balance for the next period
            balance -= principal
            # NULL THE ACCRUED INTEREST
            accrued_interest = 0
            schedule.append({
                'period': period,
                'date': monthly_due_date,
                'interest': interest,
                'fees': FEES,
                'principal': principal,
                'total_amount': total_amount,
            })

            # print(schedule)

        else:
            # Add interst to accrued_interest
            accrued_interest = interest + accrued_interest
            schedule.append({
                'period': period,
                'date': monthly_due_date,
                'interest': "-",
                'fees': "-",
                'principal': "-",
                'total_amount': "-",
            })

        # print("Accrued Interest: ", accrued_interest)

        # # update the due date for the next period
        # prev_due_date = due_date
    return schedule
