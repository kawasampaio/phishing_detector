from flask import Flask, request, jsonify
import joblib
import pandas as pd
import re
from urllib.parse import urlparse

app = Flask(__name__)

# Carregar o modelo treinado
MODEL_PATH = "../model/phishing_model.pkl"
model = joblib.load(MODEL_PATH)

# Função para extrair características da URL
def extrair_caracteristicas(url):
    parsed_url = urlparse(url)
    return {
        "comprimento_url": len(url),
        "tem_https": 1 if parsed_url.scheme == "https" else 0,
        "tem_subdominio": 1 if len(parsed_url.netloc.split(".")) > 2 else 0,
        "quantidade_digitos": len(re.findall(r"\\d", url))
    }

@app.route("/verificar_url", methods=["POST"])
def verificar_url():
    data = request.get_json()
    url = data.get("url")
    
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400
    
    caracteristicas = extrair_caracteristicas(url)
    df = pd.DataFrame([caracteristicas])
    
    previsao = model.predict(df)[0]
    resultado = "phishing" if previsao == 1 else "legítima"
    
    return jsonify({"url": url, "resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)