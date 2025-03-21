from flask import Blueprint, request, jsonify
import joblib
import os

predict_bp = Blueprint("predict", __name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/phishing_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '../model/vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = [data["url"]]
    url_vectorized = vectorizer.transform(url)
    prediction = model.predict(url_vectorized)[0]

    resultado = "phishing" if prediction == 1 else "legítima"

    return jsonify({"url": url, "prediction": resultado})
