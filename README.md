# HousePricePrediction

# House Price Prediction Web App

This is a simple web application built using **Flask** that predicts house prices based on user input such as area, number of bedrooms, bathrooms, and other features. The model used for predictions is a trained machine learning model saved as a `pickle` file.

## Features
- **Predict house price**: Users can input house features like area, number of bedrooms, location, etc., and the app will predict the house price.
- **User-friendly UI**: The app provides an easy-to-use interface for input and displays the prediction on the same page.
- **Error Handling**: In case of any issues, a proper error message is shown.

## Technologies Used
- **Python**: The back-end is powered by Python and the Flask framework.
- **Flask**: Flask is used to create the web application and handle HTTP requests.
- **Pandas**: Used for data manipulation.
- **Scikit-learn**: Used for machine learning tasks like label encoding and prediction.
- **Pickle**: To load the pre-trained machine learning model and encoders.
  
## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/ankitbista483/HousePricePrediction.git
    ```

2. Navigate to the project folder:
    ```bash
    cd house-price-prediction
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that the necessary model and encoder files are placed in the correct directory:
    - `model.pkl`: The trained model.
    - `encoder_condition.pkl`: The encoder for the 'Condition' feature.
    - `encoder_location.pkl`: The encoder for the 'Location' feature.
    - `encoder_garage.pkl`: The encoder for the 'Garage' feature.

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to use the application.

## Usage

Once the app is running, go to the homepage and fill in the details of the house you'd like to predict the price for. The form includes the following fields:

- **Area**: The area of the house in square feet.
- **Bedrooms**: Number of bedrooms.
- **Bathrooms**: Number of bathrooms.
- **Floors**: Number of floors.
- **Year Built**: Year the house was built.
- **Location**: The location of the house.
- **Condition**: The condition of the house (e.g., new, old, etc.).
- **Garage**: Whether the house has a garage or not.
- **House Age**: The age of the house.

After clicking "Predict", the predicted price will be displayed on the same page.

## Example

### Input:

- Area: 750 sq.ft
- Bedrooms: 2
- Bathrooms: 1
- Floors: 1
- Year Built: 1999
- Location: 2
- Condition: 2
- Garage: 1
- House Age: 23

### Output:
Predicted House Price: $631,441.67

## Error Handling

In case an invalid input is provided or there's any other error in processing, an error message will be displayed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
