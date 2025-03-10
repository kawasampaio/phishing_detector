import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import dask.dataframe as dd

# Carregar o dataset
DATASET_PATH = "../data/dataset_final.csv"
df = dd.read_csv(DATASET_PATH)

# Definir features e labels
X = df.drop(columns=["url", "label"])
y = df["label"]

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar o modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

# Salvar o modelo treinado
MODEL_PATH = "phishing_model.pkl"
joblib.dump(model, MODEL_PATH)
print(f"Modelo salvo em {MODEL_PATH}")