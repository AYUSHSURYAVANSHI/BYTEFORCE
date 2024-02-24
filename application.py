from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the scaler and model
scaler = pickle.load(open("Model/standardScalar.pkl", "rb"))
model = pickle.load(open("Model/modelForPrediction.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Extracting data from the form
        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        # Scaling the input data
        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Making prediction
        prediction = model.predict(new_data)

        # Determining the result
        result = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'

        return render_template('single_prediction.html', result=result)
    else:
        return render_template('index.html')  # Handle GET requests gracefully

if __name__ == "__main__":
    app.run(host="0.0.0.0")
