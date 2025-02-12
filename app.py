from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('/Users/ankitbista/Desktop/practice/HousePricePrediction/src/component/encoder_location.pkl', 'rb') as f:
    encoder_location = pickle.load(f)

with open('/Users/ankitbista/Desktop/practice/HousePricePrediction/src/component/encoder_condition.pkl', 'rb') as f:
    encoder_condition = pickle.load(f)

with open('/Users/ankitbista/Desktop/practice/HousePricePrediction/src/component/encoder_garage.pkl', 'rb') as f:
    encoder_garage = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        input_values = [
            float(request.form['Area']),
            int(request.form['Bedrooms']),
            float(request.form['Bathrooms']),
            int(request.form['Floors']),
            int(request.form['YearBuilt']),
            request.form['Location'],  
            request.form['Condition'],  
            request.form['Garage'],     
            int(request.form['HouseAge'])  
        ]
        
        
        columns = ['Area', 'Bedrooms', 'Bathrooms', 'Floors', 'YearBuilt', 'Location',  'Condition', 'Garage', 'HouseAge']
        input_df = pd.DataFrame([input_values], columns=columns)

        input_df['Location'] = encoder_location.transform(input_df['Location'])
        input_df['Condition'] = encoder_condition.transform(input_df['Condition'])
        input_df['Garage'] = encoder_garage.transform(input_df['Garage'])
   
        input_df = pd.get_dummies(input_df, drop_first=True)
     
        prediction = model.predict(input_df)

        predicted_price = round(prediction[0], 2)

    
        return render_template('index.html', prediction=predicted_price)
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)






