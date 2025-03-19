document.getElementById("checkUrl").addEventListener("click", async function() {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const url = tab.url;

    const response = await fetch(`http://localhost:5000/check_url?url=${encodeURIComponent(url)}`);
    const data = await response.json();

    document.getElementById("status").textContent = data.is_phishing ? "⚠️ Este site é perigoso!" : "✅ Site seguro!";
});
