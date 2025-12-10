# 🤖 MATIČÁK - Matiční AI Pomocník

Inteligentní školní chatbot pro Matiční gymnázium Ostrava.

## 🌐 Live Demo

**Chatbot je online!** Vyzkoušej si ho:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

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

### GitHub Pages Deployment

**👉 Aktivuj GitHub Pages a sdílej chatbot s ostatními!**

**Rychlý návod:** [GITHUB_PAGES_QUICKSTART.md](GITHUB_PAGES_QUICKSTART.md) ← **ZAČNI TADY!**

**Kroky (2 minuty):**
1. Jdi na [Settings → Pages](https://github.com/tmutina79-png/chatbot-rag-ready/settings/pages)
2. Nastav Branch: `main`, Folder: `/docs`
3. Klikni **Save**
4. Hotovo! URL: `https://tmutina79-png.github.io/chatbot-rag-ready/`

**Aktualizace webu:**
```bash
./deploy_to_pages.sh  # Automaticky zkopíruje a pushne změny
```

### Backend Deployment (volitelné)

Pro plnou funkčnost chatbota s AI a databází:

**Kompletní návod:** [DEPLOYMENT.md](DEPLOYMENT.md)

**Rychlý přehled:**
1. Deploy backend na Render.com (zdarma)
2. Aktualizuj URL v `docs/config.js`
3. Push změny
4. Chatbot má plnou funkčnost!

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
