from db import connect_db
from datetime import datetime

def insert_from_file():
    db = connect_db()
    collection = db["urls"]

    with open("urls.txt", "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]  # Remove linhas vazias

    urls = []
    for line in lines:
        parts = line.split(" - ")
        url = parts[0].strip()

        if url and url.startswith("http"):
            urls.append({
                "url": url,
                "data_adicao": datetime.utcnow()
            })
        else:
            print(f"⚠️ Ignorando linha inválida: {line}")

    if urls:
        result = collection.insert_many(urls)
        print(f"✅ {len(result.inserted_ids)} URLs inseridas!")
    else:
        print("🚫 Nenhuma URL válida para inserir.")

if __name__ == "__main__":
    insert_from_file()
