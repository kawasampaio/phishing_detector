import dask.dataframe as dd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

dataset_path = 'C:/Users/Pichau/Desktop/phishing_detector/projeto-mongo/urls.txt'


print("🔄 Carregando dataset com Dask...")
df = dd.read_csv(dataset_path)

df = df.compute()  # Converte o Dask DataFrame para Pandas
X = df['url']  # URLs como entrada
y = df['label']  # Labels (0 = legítimo, 1 = phishing)

# Vetorização das URLs
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

print("🚀 Treinando modelo...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Salvando o modelo
joblib.dump(model, 'model/phishing_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')


print("✅ Modelo treinado e salvo com sucesso!")