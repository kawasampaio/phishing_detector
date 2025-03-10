import pandas as pd

# Criando um pequeno dataset com URLs legítimas e de phishing
data = {
    "url": [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.github.com",
        "http://phishing-example.com",
        "https://secure-login.paypal.com",
        "http://fakebank-login.com",
        "https://www.linkedin.com",
        "http://malicious-site.xyz",
        "https://twitter.com",
        "http://fraud-payment.com"
    ],
    "label": [0, 0, 0, 1, 0, 1, 0, 1, 0, 1]  # 0 = legítimo, 1 = phishing
}

# Criando um DataFrame e salvando como CSV
df = pd.DataFrame(data)
df.to_csv("data/dataset_final.csv", index=False)

print("✅ Dataset de teste criado com sucesso!")
