from banco_dados.db import connect_db
from datetime import datetime
import os

def insert_from_file():
    db = connect_db()
    collection = db["urls"]

    file_path = os.path.join(os.path.dirname(__file__), "urls.txt")
    print(f"Tentando abrir o arquivo: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]  # Remove linhas vazias

    urls = []
    for line in lines:
        parts = line.split(" - ")
        if len(parts) != 2:
            print(f"Linha inválida ignorada: {line}")
            continue

        url = parts[0].strip()
        try:
            label = int(parts[1].strip())  # Converte o rótulo para inteiro (0 ou 1)
        except ValueError:
            print(f"Rótulo inválido ignorado: {line}")
            continue

        if url and url.startswith("http"):
            urls.append({
                "url": url,
                "label": label,
                "data_adicao": datetime.utcnow()
            })
        else:
            print(f"⚠️ Ignorando URL inválida: {url}")

    if urls:
        collection.insert_many(urls)
        print(f" {len(urls)} URLs inseridas com sucesso no MongoDB!")
    else:
        print(" Nenhuma URL válida para inserir.")

if __name__ == "__main__":
    insert_from_file()
