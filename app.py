from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('diabetic.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/classification', methods=['POST'])
def classification_page():
    return render_template('classification.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['Pregnancies']
    data2 = request.form['Glucose']
    data3 = request.form['BloodPressure']
    data4 = request.form['SkinThickness']
    data5 = request.form['Insulin']
    data6 = request.form['BMI']
    data7 = request.form['DiabetesPedigreeFunction']
    data8 = request.form['Age']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    pred = model.predict(arr)
    return render_template('classification.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















