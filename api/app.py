import sys
import os
import joblib
from flask import Flask, request, jsonify
from routes.predict import predict_bp
from flask_cors import CORS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
CORS(app)

# Registrar as rotas do Blueprint
app.register_blueprint(predict_bp, url_prefix="/api")

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/phishing_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '../model/vectorizer.pkl')

print("Carregando modelo...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print(" Modelo carregado com sucesso!")

@app.route("/check_url", methods=["GET"])
def check_url():
    url = request.args.get("url")
    
    if not url:
        return jsonify({"erro": "Nenhuma URL fornecida"}), 400
    
    url_vectorized = vectorizer.transform([url])
    prediction = model.predict(url_vectorized)[0]

    resultado = "perigoso" if prediction == 1 else "seguro"

    return jsonify({"url": url, "resultado": resultado})

if __name__ == '__main__':
    print("✅ Servidor rodando em http://127.0.0.1:5000")
    app.run(debug=True)
