# 🌐 GitHub Pages Deployment

## 🎯 Účel
Tento dokument obsahuje kompletní návod pro nasazení chatbota MATIČÁK na GitHub Pages, což ti umožní sdílet chatbota s ostatními na veřejné URL.

## 📍 Tvoje URL po nasazení
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

## ⚙️ Postup nasazení

### 1️⃣ Aktivace GitHub Pages

1. Otevři svůj GitHub repozitář: https://github.com/tmutina79-png/chatbot-rag-ready
2. Klikni na **Settings** (Nastavení)
3. V levém menu najdi **Pages**
4. V sekci **Source** (Zdroj):
   - **Branch**: vyber `main`
   - **Folder**: vyber `/docs`
   - Klikni **Save**

5. Počkej 1-2 minuty - GitHub vytvoří tvou stránku
6. Obnovíš stránku a nahoře uvidíš: "Your site is published at https://tmutina79-png.github.io/chatbot-rag-ready/"

### 2️⃣ Struktura souborů pro GitHub Pages

```
docs/
├── index.html        # Úvodní stránka s popisem
├── chat.html         # Samotný chatbot
└── config.js         # Konfigurace API
```

✅ **Tyto soubory jsou už připravené!**

### 3️⃣ Push změn na GitHub

```bash
cd /Users/tomasmutina/Documents/Chatbot_skola_1

# Přidej soubory
git add docs/

# Commit
git commit -m "🚀 Add GitHub Pages deployment"

# Push na GitHub
git push origin main
```

### 4️⃣ Konfigurace backendu (volitelné)

Pokud chceš, aby chatbot fungoval s tvým backendem, musíš:

1. **Nasadit backend** (např. na Render.com - viz [DEPLOYMENT.md](../DEPLOYMENT.md))

2. **Aktualizovat config.js**:
   ```javascript
   const CONFIG = {
       API_BASE_URL: 'https://tvoje-backend-url.onrender.com'
   };
   ```

3. **Push změn**:
   ```bash
   git add docs/config.js
   git commit -m "Update API URL for production"
   git push origin main
   ```

## 🎨 Co obsahuje landing page (index.html)

- ✅ Přehledný úvod k chatbotovi
- ✅ Seznam funkcí (Kontakty, Jídelna, Rozvrh, AI Chat)
- ✅ Tlačítko "Spustit Chatbota" → přesměruje na chat.html
- ✅ Status checker - kontroluje, jestli je backend online
- ✅ Odkazy na GitHub repository
- ✅ Responzivní design (funguje na mobilu i PC)

## 🔗 Jak sdílet s ostatními

Po aktivaci GitHub Pages můžeš sdílet tyto URL:

### Hlavní stránka (doporučeno pro sdílení):
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

### Přímý odkaz na chatbota:
```
https://tmutina79-png.github.io/chatbot-rag-ready/chat.html
```

## 📱 Testování

1. Otevři URL v prohlížeči
2. Zkontroluj, že se načte landing page
3. Klikni na "Spustit Chatbota"
4. Ověř, že chatbot funguje

## 🐛 Řešení problémů

### Stránka se nenačítá (404 Error)
- Počkej 2-3 minuty po aktivaci GitHub Pages
- Zkontroluj, že máš správně nastavenou složku `/docs` v Settings → Pages
- Ověř, že soubory jsou na GitHubu: https://github.com/tmutina79-png/chatbot-rag-ready/tree/main/docs

### Chatbot nefunguje
- Je to normální! Backend běží lokálně na tvém počítači
- Pro plnou funkčnost musíš nasadit backend (viz [DEPLOYMENT.md](../DEPLOYMENT.md))
- Nebo lze použít demo režim (frontend-only funkce)

### CORS chyby v konzoli
- To je očekávané, pokud backend není nasazený
- Status bar na stránce upozorní: "Backend server je momentálně offline"

## 🎯 Další kroky

1. ✅ **Nasadit backend** - viz [DEPLOYMENT.md](../DEPLOYMENT.md)
2. ✅ **Aktualizovat API URL** v `docs/config.js`
3. ✅ **Testovat vše** včetně API volání
4. ✅ **Sdílet URL** s učiteli a studenty!

## 💡 Tipy

- **Custom doména**: V GitHub Pages můžeš nastavit vlastní doménu (např. maticak.cz)
- **Analytics**: Můžeš přidat Google Analytics pro sledování návštěvnosti
- **PWA**: Lze rozšířit o Progressive Web App pro instalaci jako mobilní aplikace

## 📞 Potřebuješ pomoc?

- GitHub Pages dokumentace: https://docs.github.com/pages
- Render.com pro backend: https://render.com/docs
- Nahlásit problém: https://github.com/tmutina79-png/chatbot-rag-ready/issues
