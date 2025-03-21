from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")

def connect_db():
    try:
        client = MongoClient(MONGO_URI)
        db = client["Urls"] 
        print("Conectado ao MongoDB!")
        return db
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    connect_db()
