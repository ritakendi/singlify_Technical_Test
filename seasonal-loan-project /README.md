# Loan Schedule Calculation App using Flask.

This is a simple web application built with Flask that calculates a loan repayment schedule based on user input. The app allows the user to enter loan details such as loan amount, number of months, expected disbursement date, and select months to repay the loan.

## Getting Started

1. Clone the repository:

    git clone https://github.com/ritakendi/singlify_Technical_Test.git

2. Change directory to the project folder:

    cd seasonal-loan-project

3. Install the required dependencies:
    pip install -r requirements.txt

4. Run the Flask app:
    python app.py

5. Open your web browser and navigate   to http://localhost:5000/.

## Usage
1. Enter the loan details in the form fields provided.
2. Select the months to repay the loan.
3. Click on the Calculate Schedule button to calculate the loan repayment schedule.
4. The loan repayment schedule will be displayed on the same page.

## File Structure
The project contains the following files:

1. app.py: This is the main Flask application file that contains the loan calculation logic.
calculation.py: This file contains the 2. loan calculation functions that are imported into app.py.
3. templates/home.html: This is the HTML template that is rendered by Flask to display the loan calculation form and results.