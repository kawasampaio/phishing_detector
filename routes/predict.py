from flask import Blueprint, request, jsonify

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "Nenhuma URL fornecida"}), 400

    return jsonify({"url": url, "prediction": "phishing"})  # Apenas um exemplo
