# Titanic Survival Prediction 🚢

This is a Flask web application that predicts whether a passenger survived the Titanic disaster based on their details like gender, class, age, fare, etc. The prediction is powered by a trained Logistic Regression model.

## 🗂 Project Structure

```
titanic-survival-prediction/
├── app.py                        # Flask app
├── logistic_regression_model.pkl # Trained ML model
├── templates/
│   └── template.html             # Frontend HTML form
├── train.csv                     # Training dataset (optional)
├── test.csv                      # Testing dataset (optional)
├── titanic-survival-prediction.ipynb # Jupyter notebook for training
└── requirements.txt              # Python dependencies
```

## 🚀 How to Run the App

### Step 1: Clone the Repository
```bash
git clone https://github.com/mesumitsingh/titanic-survival-prediction.git
cd titanic-survival-prediction
```

### Step 2: Create and Activate Virtual Environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# OR
source venv/bin/activate    # On macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask App
```bash
python app.py
```

The app will run at: []()


## 📥 Inputs Required

- Gender: 0 for Female, 1 for Male  
- Passenger Class: 1 (Upper), 2 (Middle), 3 (Lower)  
- Age, Fare, SibSp, Parch  
- Embarked: 0 = Cherbourg, 1 = Queenstown, 2 = Southampton

## 🧠 Model

The model is a Logistic Regression classifier trained on the Titanic dataset (train.csv) and saved as `logistic_regression_model.pkl`.

## 📸 UI Preview

> Add a screenshot here if desired!

## 📜 License

MIT License

---

Made with ❤️ using Flask and Machine Learning!