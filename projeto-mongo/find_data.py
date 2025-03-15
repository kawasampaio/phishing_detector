from db import connect_db

def find_data():
    db = connect_db()
    collection = db["urls"]

    urls = list(collection.find())
    for url in urls:
        print(url)

if __name__ == "__main__":
    find_data()
