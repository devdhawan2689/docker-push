from flask import Flask, render_template, request
import pandas as pd
import pickle 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runModel', methods=['GET', 'POST'])
def runModel():
    Married = request.args.get('married')
    Education = request.args.get('education')
    ApplicantIncome = request.args.get('applicantincome')
    LoanAmount = request.args.get('loanamount')
    Credit_History = request.args.get('credithistory')

    print(Married, Education, ApplicantIncome, LoanAmount, Credit_History)

    model = pickle.load(open('Complete_Model.pkl', 'rb')) 

    test = pd.DataFrame([[Married, Education, ApplicantIncome, LoanAmount, Credit_History]], columns = ['Married', 'Education', 'ApplicantIncome', 'LoanAmount', 'Credit_History'])
    test

    prediction = model.predict(test) 

    return str(prediction[0])

@app.route('/runModel2', methods=['GET', 'POST'])
def runModel2():
    Married = request.form['married']
    Education = request.form['education']
    ApplicantIncome = request.form['applicantincome']
    LoanAmount = request.form['loanamount']
    Credit_History = request.form['credithistory']

    print(Married, Education, ApplicantIncome, LoanAmount, Credit_History)

    model = pickle.load(open('Complete_Model.pkl', 'rb')) 

    test = pd.DataFrame([[Married, Education, ApplicantIncome, LoanAmount, Credit_History]], columns = ['Married', 'Education', 'ApplicantIncome', 'LoanAmount', 'Credit_History'])
    test

    prediction = model.predict(test) 

    return str(prediction[0])

# main driver function
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000) 