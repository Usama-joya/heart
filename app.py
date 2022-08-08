# noinspection PyUnresolvedReferences
from flask import Flask, request, jsonify
import pickle
import numpy as np


model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict' , methods=['POST'] )
def predict():
    Age = request.form.get('Age')
    Gender = request.form.get('Gender')
    Cp = request.form.get('Cp')
    Trestbps = request.form.get('Trestbps')
    Chol = request.form.get('Chol')
    Fbs = request.form.get('Fbs')
    Restecg = request.form.get('Restecg')
    Thalach = request.form.get('Thalach')
    Exang = request.form.get('Exang')
    Oldpeak = request.form.get('Oldpeak')
    Slope = request.form.get('Slope')
    Ca = request.form.get('Ca')
    Thal = request.form.get('Thal')

    input_query = np.array([[Age,Gender,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]])

    result = model.predict(input_query)[0]

    return jsonify({'You have heart disease':str(result)})



if __name__ =='__main__':
    app.run(debug=True)