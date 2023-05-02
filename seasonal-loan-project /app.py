from flask import Flask, render_template, request
from calculation import calculate_loan_schedule
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculate_schedule', methods=['POST'])
def calculate_schedule():
    print("success")
    # extract data from form

    loan_product = request.form.get('loan_product')
    loan_amount = float(request.form.get('loan_amount'))
    num_months = int(request.form.get('num_months'))
    Expected_Disbursement_Date = request.form.get('Expected_Disbursement_Date')
    Expected_Disbursement_Date = datetime.strptime(
        Expected_Disbursement_Date, '%Y-%m-%d').date()

    select_months = request.form.getlist('months')
    periods_per_year = len(select_months)

    # interest = float(request.form['interest'])
    # admin_fee = 0.35
    # loan_term = int(request.form['term'])
    # monthly_due_date = datetime.strptime('2023-05-02', '%Y-%m-%d').date()
    due_date = int(request.form.get('due_date'))

    interest_rate = 10.90

    schedule = calculate_loan_schedule(
        num_months, loan_amount, periods_per_year, Expected_Disbursement_Date, due_date, loan_product, select_months)

    return render_template('home.html', schedule=schedule)


if __name__ == "__main__":
    app.run(debug=True)
