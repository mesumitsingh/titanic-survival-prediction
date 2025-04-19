from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Logistic Regression model
import joblib

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model.pkl')

@app.route('/')
def home():
    return render_template('template.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data and convert to float
        gender = float(request.form['gender'])          # 0 for female, 1 for male
        pclass = float(request.form['pclass'])          # 1, 2, or 3
        age = float(request.form['age'])                # Age in years
        sibsp = float(request.form['sibsp'])            # # of siblings/spouses aboard
        parch = float(request.form['parch'])            # # of parents/children aboard
        fare = float(request.form['fare'])              # Ticket fare
        embarked = float(request.form['embarked'])      # 0 = C, 1 = Q, 2 = S

        # Create a NumPy array from input
        input_data = np.array([[gender, pclass, age, sibsp, parch, fare, embarked]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        result = "Survived" if prediction == 1 else "Did not survive"
        return render_template('template.html', prediction_text=f'Prediction: {result}')
    
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)