from flask import Blueprint, request, jsonify
import joblib

predict_bp = Blueprint('predict', __name__)

# Carregar modelo
model = joblib.load("model/phishing_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = [data['url']]
    url_vectorized = vectorizer.transform(url)
    prediction = model.predict(url_vectorized)[0]

    return jsonify({"prediction": int(prediction)})
