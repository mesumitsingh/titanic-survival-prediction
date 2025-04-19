
# 🚢 Titanic Survival Prediction

A Flask web application that predicts whether a passenger survived the Titanic disaster based on their details like gender, class, age, fare, etc. The prediction is powered by a trained **Logistic Regression** model.

---

## 🗂 Project Structure

```
titanic-survival-prediction/
├── app.py                      # Flask app
├── logistic_regression_model.pkl  # Trained ML model
├── templates/
│   └── template.html          # Frontend HTML form
├── train.csv                  # Training dataset (optional)
├── test.csv                   # Testing dataset (optional)
├── titanic-survival-prediction.ipynb  # Jupyter notebook for training
└── requirements.txt           # Python dependencies
```

---

## 🚀 How to Run the App

### Step 1: Clone the Repository
```bash
git clone https://github.com/mesumitsingh/titanic-survival-prediction.git
cd titanic-survival-prediction
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask App
```bash
python app.py
```
The app will start at: [http://localhost:5000](http://localhost:5000)

### Step 4: Open the UI

Open your browser and navigate to [http://localhost:5000](http://localhost:5000).  
You will see a form where you can enter passenger details and make survival predictions.

---

## 📥 Inputs Required

- **Gender**: `0` for Female, `1` for Male  
- **Passenger Class**: `1` = Upper, `2` = Middle, `3` = Lower  
- **Age**: e.g., `29`  
- **Fare**: e.g., `72.50`  
- **SibSp**: Number of siblings/spouses aboard  
- **Parch**: Number of parents/children aboard  
- **Embarked**: `0` = Cherbourg, `1` = Queenstown, `2` = Southampton  

---

## 🧠 Model

The app uses a **Logistic Regression** model trained on the Titanic dataset (`train.csv`) and saved as `logistic_regression_model.pkl`.

---

## 📸 UI Preview

> ![UI Preview](static/preview.png)


---

## 🌐 Use It Now

Visit the live app here: [Titanic Survival Prediction](https://titanic-survival-prediction-e705.onrender.com)
> https://titanic-survival-prediction-e705.onrender.com

---

## 📜 License

This project is licensed under the **MIT License**.

---

Made with ❤️ using **Flask** and **Machine Learning**
