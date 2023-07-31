from flask import Flask,request,app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model= pickle.load(open('/config/workspace/Model/decisiontreeRegressorModel.pkl','rb'))

# route for homepage


@app.route('/')
def index():
    return render_template('index.html')

# Route for single data point prediction
@app.route('/predictdata',methods= ['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':
        

        
        MedInc=float(request.form.get('MedInc'))
        HouseAge=float(request.form.get('HouseAge'))
        AveRooms=float(request.form.get('AveRooms'))
        AveBedrms=float(request.form.get('AveBedrms'))
        Population=float(request.form.get('Population'))
        AveOccup=float(request.form.get('AveOccup'))
        Latitude=float(request.form.get('Latitude'))
        Longitude=float(request.form.get('Longitude'))

        new_data = [[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]]

        predict = model.predict(new_data)

        return render_template('singlePrediction.html',result=predict)

    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)           




