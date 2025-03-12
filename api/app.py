import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from routes.predict import predict_bp
from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

app.register_blueprint(predict_bp)
if __name__ == '__main__':
    app.run(debug=True)

# Caminhos dos modelos
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/phishing_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '../model/vectorizer.pkl')

# Carregar modelo treinado e vetorizador
print("🔄 Carregando modelo...")
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)
print("✅ Modelo carregado com sucesso!")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url', '')
    
    if not url:
        return jsonify({'error': 'Nenhuma URL fornecida'}), 400
    
    # Transformar a URL com o vetorizador
    url_vectorized = vectorizer.transform([url])
    
    # Fazer a previsão
    prediction = model.predict(url_vectorized)[0]
    resultado = "phishing" if prediction == 1 else "legítima"
    
    return jsonify({'url': url, 'prediction': resultado})

if __name__ == '__main__':
    app.run(debug=True)
