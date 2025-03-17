from projeto_mongo.db import connect_db  # Importa a conexão com o MongoDB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import numpy as np

# Conectar ao banco de dados
db = connect_db()
collection = db["urls"]

# Buscar todas as URLs salvas no MongoDB
print("🔄 Buscando dados do MongoDB...")
urls = list(collection.find({}, {"_id": 0, "url": 1}))  # Pegamos apenas a URL

if not urls:
    raise ValueError("⚠️ Nenhuma URL encontrada no banco de dados!")

# Extrair URLs como lista de strings
X = [item["url"] for item in urls]

# Assumimos que todas as URLs no MongoDB são legítimas (label = 0)
y = np.zeros(len(X), dtype=int)

# Vetorização das URLs
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Treinar o modelo
print("🚀 Treinando modelo...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Salvando o modelo
joblib.dump(model, "model/phishing_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Modelo treinado e salvo com sucesso!")
