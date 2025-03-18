from banco_dados.db import connect_db
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import numpy as np

db = connect_db()
collection = db["urls"]

print("🔍 Buscando dados do MongoDB...")
data = list(collection.find({}, {"_id": 0, "url": 1, "label": 1}))

if not data:
    raise ValueError("⚠️ Nenhuma URL encontrada no banco de dados!")

X = [item["url"] for item in data]  
y = [item["label"] for item in data]  

# Vetorização das URLs
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Dividir em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

print("🚀 Treinando modelo...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ Modelo treinado com precisão de {accuracy * 100:.2f}%")

# Salvar modelo e vetorizar no disco
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("🎯 Modelo salvo com sucesso!")
