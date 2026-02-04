// Konfigurace API endpointů
const CONFIG = {
    // Automatická detekce prostředí
    API_BASE_URL: (window.location.protocol === 'file:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
        ? 'http://127.0.0.1:8001'  // Lokální vývoj - změněno na port 8001
        : 'https://deploy-web-service-enfc.onrender.com',  // Produkční backend na Render.com
    
    // Alternativně můžeš nastavit přímo:
    // API_BASE_URL: 'http://127.0.0.1:8001'  // Pro lokální testování
    // API_BASE_URL: 'https://deploy-web-service-enfc.onrender.com'  // Pro produkci
};
