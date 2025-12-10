# 🚀 Nasazení Chatbota - Krok za Krokem

## ✅ Co už máme hotové
- ✅ JSON databáze s daty školy (`data/skolni_data.json`)
- ✅ DataManager pro spolehlivé načítání dat
- ✅ Všechny endpointy fungují s databází jako fallback
- ✅ Změny commitnuté a pushnuté na GitHub
- ✅ render.yaml připraven pro auto-deploy

## 📋 Zbývající kroky

### Krok 1: Registrace na Render.com (2 minuty)
1. Otevři https://render.com
2. Klikni na **"Get Started for Free"**
3. Vyber **"Sign Up with GitHub"**
4. Autorizuj Render.com přístup k tvému GitHub účtu
5. Vyber repository: **tmutina79-png/chatbot-rag-ready**

### Krok 2: Vytvoření Web Service (3 minuty)
1. Po přihlášení klikni na **"New +"** → **"Web Service"**
2. Najdi a vyber: **chatbot-rag-ready**
3. Vyplň detaily:
   - **Name**: `chatbot-backend` (nebo libovolný název)
   - **Region**: `Frankfurt (EU Central)` (nejbližší k ČR)
   - **Branch**: `main`
   - **Root Directory**: nech prázdné
   - **Runtime**: automaticky detekuje Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: **Free**

4. Klikni na **"Create Web Service"**

### Krok 3: Čekání na Build (5-10 minut)
Render.com automaticky:
- Naklonuje tvůj GitHub repo
- Nainstaluje všechny závislosti z `requirements.txt`
- Spustí FastAPI server
- Přidělí veřejnou URL (např. `https://chatbot-backend-xyz.onrender.com`)

**Sleduj log v reálném čase:**
```
==> Installing dependencies...
==> Building...
==> Starting service...
==> Your service is live at https://chatbot-backend-xyz.onrender.com
```

### Krok 4: Test Backendu (1 minuta)
Zkopíruj svou Render.com URL a otestuj v prohlížeči nebo terminálu:

```bash
# Zkopíruj svou URL z Render.com (např. https://chatbot-backend-xyz.onrender.com)
BACKEND_URL="https://chatbot-backend-xyz.onrender.com"

# Test vedení školy
curl "$BACKEND_URL/kontakt/vedeni"

# Test dnešního menu
curl "$BACKEND_URL/jidelna/dnesni-menu"

# Test rozvrhu
curl "$BACKEND_URL/rozvrh/kva"
```

**Očekávaný výsledek**: JSON data s `"success": true` a `"source": "database"` nebo `"source": "scraping"`

### Krok 5: Aktualizace GitHub Pages Config (2 minuty)
1. Otevři soubor `docs/config.js` v editoru
2. Najdi řádek:
   ```javascript
   const API_URL = "http://127.0.0.1:8000";
   ```
3. Změň na svou Render.com URL:
   ```javascript
   const API_URL = "https://chatbot-backend-xyz.onrender.com";
   ```
4. Ulož soubor
5. Commit a push:
   ```bash
   git add docs/config.js
   git commit -m "Aktualizace API URL na Render.com backend"
   git push origin main
   ```

### Krok 6: Aktivace GitHub Pages (pokud ještě není aktivní)
1. Otevři https://github.com/tmutina79-png/chatbot-rag-ready/settings/pages
2. V sekci **"Source"** vyber:
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Klikni **"Save"**
4. Počkej 1-2 minuty
5. GitHub Pages bude dostupný na: **https://tmutina79-png.github.io/chatbot-rag-ready/**

### Krok 7: Finální Test (1 minuta)
1. Otevři https://tmutina79-png.github.io/chatbot-rag-ready/
2. Klikni na **"Otevřít chatbota"**
3. Vyzkoušej tlačítka:
   - **Vedení školy**
   - **Dnešní menu**
   - **Rozvrh KVA**
4. Všechno by mělo fungovat! 🎉

## 🎯 Hotovo!
Tvůj chatbot je nyní online a dostupný pro celý svět na:
- **Chatbot**: https://tmutina79-png.github.io/chatbot-rag-ready/
- **Backend API**: https://tvoje-url.onrender.com

## 🔧 Důležité poznámky

### Render.com Free Tier omezení:
- ⏰ **Automatické vypnutí po 15 minutách nečinnosti**
- 🐌 **První request po vypnutí trvá 30-60 sekund** (cold start)
- 💾 **750 hodin zdarma měsíčně** (postačí pro školu)
- 🌍 **Veřejná URL, žádná autentizace** (vhodné pro školní web)

### Co dělat když se chatbot zdá být pomalý:
1. První načtení po dlouhé době může trvat až minutu (Render.com "probouzí" server)
2. Další requesty už budou rychlé
3. Pro 24/7 dostupnost je třeba upgradovat na placenou verzi ($7/měsíc)

### Jak aktualizovat data:
1. Uprav `data/skolni_data.json`
2. Commit a push na GitHub
3. Render.com automaticky znovu nasadí backend (5-10 minut)

## 💡 Tipy pro údržbu

### Automatické probuzení serveru:
Můžeš nastavit službu jako UptimeRobot nebo Cronitor, která každých 14 minut pošle ping na tvůj backend, aby zůstal aktivní.

### Monitoring:
- Render.com dashboard ukazuje logy a metriky
- GitHub Actions může automaticky testovat API po každém deployi

### Další vylepšení:
- Přidat autentizaci (API klíče)
- Nastavit custom doménu (např. chatbot.skola.cz)
- Přidat rate limiting proti spamu
- Implementovat cache pro rychlejší odpovědi

---

**Máš problém?** Otevři [GitHub Issue](https://github.com/tmutina79-png/chatbot-rag-ready/issues) nebo se podívej do `RENDER_DEPLOYMENT.md` pro detailní troubleshooting.
