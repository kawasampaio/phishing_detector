document.getElementById("checkUrl").addEventListener("click", async function() {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const url = tab.url;

    try {
        const response = await fetch(`http://localhost:5000/check_url?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        if (data.resultado === "perigoso") {
            document.getElementById("status").textContent = "⚠️ Este site é perigoso!";
            alert("🚨 Cuidado! Este site pode ser uma ameaça!");
        } else {
            document.getElementById("status").textContent = "✅ Site seguro!";
        }
    } catch (error) {
        document.getElementById("status").textContent = "Erro ao verificar!";
        console.error("Erro na requisição:", error);
    }
});
