# 🌐 MATIČÁK - Web Deployment

Tato složka obsahuje soubory pro GitHub Pages deployment.

## 📁 Soubory

- **index.html** - Úvodní landing page s popisem chatbota
- **chat.html** - Samotný chatbot widget
- **config.js** - Konfigurace API endpointů
- **GITHUB_PAGES_SETUP.md** - Kompletní návod na nasazení
- **CUSTOM_DOMAIN.md** - Návod na vlastní doménu

## 🚀 URL

Po nasazení bude dostupné na:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

## ⚙️ Jak nasadit

Kompletní návod najdeš v [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)

## 🔄 Aktualizace

Pro aktualizaci chatbota na webu:

```bash
# 1. Zkopíruj nejnovější verzi z app/ui/
cp app/ui/chat.html docs/chat.html

# 2. Commit a push
git add docs/
git commit -m "Update chatbot"
git push origin main

# 3. Změny se projeví do 1-2 minut
```

## 🎨 Přizpůsobení

### Landing Page (index.html)
- Uprav text, barvy, funkce
- Změň odkazy na GitHub
- Přidej logo školy

### API Konfigurace (config.js)
- Pro lokální vývoj: `http://127.0.0.1:8000`
- Pro produkci: `https://tvoje-backend-url.onrender.com`

## 📞 Podpora

- [GitHub Pages dokumentace](https://docs.github.com/pages)
- [Nahlásit problém](https://github.com/tmutina79-png/chatbot-rag-ready/issues)
