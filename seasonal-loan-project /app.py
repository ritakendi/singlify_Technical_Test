# Import necessary libraries and modules
from flask import Flask, render_template, request
from calculation import calculate_loan_schedule
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# define home route


@app.route('/')
def home():
    return render_template('home.html')

# Define route for calculating loan schedule


@app.route('/calculate_schedule', methods=['POST'])
def calculate_schedule():

    # extract data from form submitted by user
    loan_product = request.form.get('loan_product')
    loan_amount = float(request.form.get('loan_amount'))
    num_months = int(request.form.get('num_months'))
    Expected_Disbursement_Date = request.form.get('Expected_Disbursement_Date')
    Expected_Disbursement_Date = datetime.strptime(
        Expected_Disbursement_Date, '%Y-%m-%d').date()
    select_months = request.form.getlist('months')
    periods_per_year = len(select_months)
    due_date = int(request.form.get('due_date'))

    # calculate loan repayment schedule based on user input
    schedule = calculate_loan_schedule(
        num_months, loan_amount, periods_per_year, Expected_Disbursement_Date, due_date, loan_product, select_months)

    print('AWesome')
    # render home template with loan schedule data to be displayed to the user
    return render_template('home.html', schedule=schedule)


# run Flask app
if __name__ == "__main__":
    app.run(debug=True)
