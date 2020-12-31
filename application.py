import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    new_data={'CRIM':[int_features[0]],'RM':[int_features[1]],'LSTAT':[int_features[2]]}
    prediction = model.predict(pd.DataFrame(data=new_data,columns=['CRIM', 'RM', 'LSTAT']))

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Prediction is $ {}'.format(output))

@app.route('/results',methods=['POST'])   
def results():

    data = request.json   #request.get_json(force=True)
    prediction1 = list(data.values())
    int_features = [int(x) for x in prediction1]
    
    new_data={'CRIM':[int_features[0]],'RM':[int_features[1]],'LSTAT':[int_features[2]]}
    prediction = model.predict(pd.DataFrame(data=new_data,columns=['CRIM', 'RM', 'LSTAT']))
    
    output = int(prediction[0]) #can deliver only integers !!! (jsonify)
    
    return jsonify({"r":output})   #output)

if __name__ == "__main__":
    app.run(debug=True)