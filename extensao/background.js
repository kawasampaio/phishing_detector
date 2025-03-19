chrome.webRequest.onBeforeRequest.addListener(
    async function(details) {
        const url = details.url;

        try {
            const response = await fetch(`http://localhost:5000/check_url?url=${encodeURIComponent(url)}`);
            const data = await response.json();

            if (data.is_phishing) {
                return { redirectUrl: "https://www.google.com/search?q=site+malicioso+detectado" }; // Redireciona o usuário
            }
        } catch (error) {
            console.error("Erro ao verificar URL:", error);
        }

        return { cancel: false };
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
);
