import requests
import pandas as pd
import random

# URL da API do OpenPhish para coletar URLs maliciosas
URL_OPENPHISH = "https://openphish.com/feed.txt"

# Lista de alguns sites confiáveis para criar um conjunto de URLs legítimas
URLS_LEGITIMAS = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.amazon.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.netflix.com"
]

# Função para coletar URLs de phishing
def coletar_urls_phishing():
    response = requests.get(URL_OPENPHISH)
    if response.status_code == 200:
        urls = response.text.split("\n")
        return urls
    else:
        print("Erro ao coletar os dados.")
        return []

# Coletar URLs de phishing
urls_phishing = coletar_urls_phishing()

# Criar DataFrame
df_phishing = pd.DataFrame(urls_phishing, columns=["url"])
df_phishing["label"] = 1  # 1 para phishing

df_legitimas = pd.DataFrame(URLS_LEGITIMAS, columns=["url"])
df_legitimas["label"] = 0  # 0 para legítimo

# Unir os datasets
df_final = pd.concat([df_phishing, df_legitimas], ignore_index=True)
random.shuffle(df_final.values.tolist())  # Embaralhar os dados

# Salvar os dados em um arquivo CSV
df_final.to_csv("dataset_final.csv", index=False)
print("Coleta concluída. Dados salvos!")
