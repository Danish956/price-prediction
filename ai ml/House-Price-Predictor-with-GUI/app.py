from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
modell=pickle.load(open("model_pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict',methods=['POST'])
def predict():
    floors = float(request.form.get('floor'))
    noofvisited =float(request.form.get('visited'))
    basementarea=float(request.form.get('basement'))
    ageofhouse =request.form.get('age')
    zipcode =float(request.form.get('zipcode'))
    latitude =float(request.form.get('latitude'))
    longitude =float(request.form.get('longitude'))
    livingareaafterreno =float(request.form.get('living'))
    lotareaafterreno =float(request.form.get('lotarea'))
    yearreno =request.form.get('yrsreno')
    bath =float(request.form.get('bathroom'))
    bed =float(request.form.get('bedroom'))
    waterfront =request.form.get('view')
    conditionofhouse =request.form.get('condition')
    grade =request.form.get('grade')
    everreno =request.form.get('everreno')

    input=pd.DataFrame([[bed,bath,floors,waterfront,noofvisited,conditionofhouse,grade,basementarea,ageofhouse,zipcode,latitude,longitude,livingareaafterreno,lotareaafterreno,everreno,yearreno]],columns=["no of bedrooms", "no of bathrooms", "no of floors", "waterfront view", "no of times visited", "condition of the house", "overall grade", "basement area (in sqft)", "age of house (in years)", "zipcode", "latitude", "longitude", "living area after renovation (in sqft)", "lot area after renovation (in sqft)", "ever renovated", "years since renovation"])
    prediction = modell.predict(input)[0]/1000
    return str(np.round(prediction,2))

if __name__=="__main__":
    app.run(debug=True)