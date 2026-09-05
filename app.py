from pathlib import Path
import pickle

import pandas as pd
from flask import Flask, jsonify, render_template_string, request

BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / "diabetes_model.sav", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)
FEATURES = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

PAGE = """<!doctype html>
<title>Diabetes Prediction</title>
<h1>Diabetes Prediction</h1>
<form method="post">
{% for feature in features %}<label>{{ feature }}<br><input name="{{ feature }}" type="number" step="any" required></label><br><br>{% endfor %}
<button type="submit">Predict</button>
</form>
{% if result %}<h2>{{ result }}</h2>{% endif %}
<p>For research and education only. This is not medical advice.</p>
"""


def predict(payload):
    values = {feature: float(payload[feature]) for feature in FEATURES}
    sample = pd.DataFrame([values], columns=FEATURES)
    prediction = int(model.predict(sample)[0])
    response = {"prediction": prediction, "label": "diabetic" if prediction else "non-diabetic"}
    if hasattr(model, "predict_proba"):
        response["confidence"] = round(float(model.predict_proba(sample).max()), 4)
    return response


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            result = predict(request.form)["label"]
        except (KeyError, TypeError, ValueError):
            result = "Please enter valid values for every field."
    return render_template_string(PAGE, features=FEATURES, result=result)


@app.post("/predict")
def api_predict():
    try:
        return jsonify(predict(request.get_json(force=True)))
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "JSON must contain all diabetes feature names."}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)
