// Konfigurace API endpointů
const CONFIG = {
    // Automatická detekce prostředí
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://127.0.0.1:8000'  // Lokální vývoj
        : 'https://deploy-web-service-enfc.onrender.com',  // Produkční backend na Render.com
    
    // Alternativně můžeš nastavit přímo:
    // API_BASE_URL: 'http://127.0.0.1:8000'  // Pro lokální testování
    // API_BASE_URL: 'https://deploy-web-service-enfc.onrender.com'  // Pro produkci
};
