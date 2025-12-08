# 🤖 MATIČÁK - Matiční AI Pomocník

Inteligentní školní chatbot pro Matiční gymnázium Ostrava.

## ✨ Funkce

- 📧 **Kontakty**: Vedení školy a učitelé dle předmětů
- 🍽️ **Jídelna**: Denní a týdenní menu s automatickým scrapingem
- 💬 **AI Chat**: Konverzační asistent postavený na RAG systému
- 🎨 **Moderní UI**: Chat widget v pravém dolním rohu

## 🚀 Rychlý start

### Lokální testování

```bash
# 1. Aktivuj virtuální prostředí
source .venv/bin/activate

# 2. Spusť backend
uvicorn main:app --reload --port 8000

# 3. Otevři frontend v prohlížeči
open app/ui/chat.html
```

### Nasazení pro účastníky

**Kompletní návod najdeš v [DEPLOYMENT.md](DEPLOYMENT.md)**

**Rychlý přehled:**
1. Deploy backend na Render.com (zdarma)
2. Aktualizuj URL v `app/ui/config.js`
3. Push na GitHub
4. Aktivuj GitHub Pages
5. Sdílej URL účastníkům

## 📝 Konfigurace

Před nasazením **MUSÍŠ** upravit `app/ui/config.js`:

```javascript
const CONFIG = {
    API_BASE_URL: 'https://tvoje-backend-url.com'  // ← ZMĚŇ TUTO URL!
};
```

## 🧪 Testování API

```bash
# Vedení školy
curl http://localhost:8000/kontakt/vedeni

# Učitelé matematiky
curl http://localhost:8000/kontakt/ucitele/matematika

# Dnešní menu
curl http://localhost:8000/jidelna/dnesni-menu

# Týdenní menu
curl http://localhost:8000/jidelna/tydenni-menu
```

API dokumentace: http://localhost:8000/docs

## 📦 Struktura

```
├── app/
│   ├── core/       # Orchestrator, RAG, databáze
│   ├── kontakty/   # Scraping učitelů
│   ├── jidelna/    # Scraping menu
│   └── ui/         # Frontend (HTML/CSS/JS)
├── main.py         # FastAPI server
└── requirements.txt
```

## 🆘 Pomoc

Podrobný návod k nasazení: [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Vytvořeno žáky Matičního gymnázia Ostrava** ❤️
