# 🎯 RYCHLÝ NÁVOD - Aktivace GitHub Pages

## ✅ Co jsem udělal

1. ✅ Vytvořil složku `docs/` s náhledem chatbota
2. ✅ Vytvořil krásnou landing page (úvodní stránku)
3. ✅ Zkopíroval chat.html do docs/
4. ✅ Commitnul a pushnul na GitHub

## 🚀 CO MUSÍŠ UDĚLAT TEĎ (5 minut)

### Krok 1: Otevři GitHub Settings
1. Jdi na: **https://github.com/tmutina79-png/chatbot-rag-ready**
2. Klikni na **Settings** (⚙️ nahoře vpravo)

### Krok 2: Aktivuj GitHub Pages
1. V levém menu najdi **Pages** (Pod "Code and automation")
2. V sekci **Source**:
   - **Branch**: vyber `main` (místo None)
   - **Folder**: vyber `/docs` (místo root)
   - Klikni **Save**

### Krok 3: Počkej 1-2 minuty
GitHub vytváří tvou stránku...

### Krok 4: Získej URL
1. Obnov stránku (F5)
2. Nahoře uvidíš: **"Your site is published at https://tmutina79-png.github.io/chatbot-rag-ready/"**
3. Klikni na URL a zkontroluj, že to funguje!

## 🎉 Hotovo!

Tvůj chatbot je nyní dostupný na:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

## 📱 Co vidí návštěvníci?

### Úvodní stránka (index.html):
- 🎨 Krásný design s gradientem
- 📝 Popis chatbota
- ✨ Seznam funkcí (Kontakty, Jídelna, Rozvrh, AI Chat)
- 🚀 Tlačítko "Spustit Chatbota"
- 🔗 Odkazy na GitHub
- ⚡ Status checker (kontroluje backend)

### Chatbot (chat.html):
- Plně funkční chatbot widget
- Všechny funkce, které máš lokálně
- Backend zatím offline (to je OK!)

## 🔥 Sdílej s ostatními!

Teď můžeš poslat tuto URL komukoli:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

## ⚠️ Poznámky

- **Backend je offline** - je to normální! Chatbot má frontend, ale backend běží jen na tvém počítači
- **Pro plnou funkčnost**: Nasaď backend na Render.com (viz DEPLOYMENT.md)
- **Status bar**: Na stránce se zobrazí, že backend je offline
- **Demo režim**: Některé funkce fungují i bez backendu

## 📚 Další dokumentace

- **Kompletní návod**: `docs/GITHUB_PAGES_SETUP.md`
- **Vlastní doména**: `docs/CUSTOM_DOMAIN.md`
- **Backend deployment**: `DEPLOYMENT.md`

## 🐛 Problémy?

### "404 - Page not found"
- Počkej 2-3 minuty po aktivaci
- Zkontroluj Settings → Pages (Branch: main, Folder: /docs)

### Stránka je prázdná
- Zkontroluj, že se files nahrály: https://github.com/tmutina79-png/chatbot-rag-ready/tree/main/docs
- Obnov browser cache (Ctrl+Shift+R nebo Cmd+Shift+R)

### Backend nefunguje
- To je OK! Status bar to upozorní
- Pro plnou funkčnost nasaď backend (viz DEPLOYMENT.md)

## 🎯 Příští kroky

1. ✅ Zkontroluj, že web funguje
2. 📤 Sdílej URL s kamarády/učiteli
3. 🚀 (Volitelně) Nasaď backend pro plnou funkčnost
4. 🎨 (Volitelně) Přizpůsob landing page (barvy, text, logo)
5. 🌐 (Volitelně) Nastav vlastní doménu (např. maticak.cz)

---

**Potřebuješ pomoc?** Nahlásit problém: https://github.com/tmutina79-png/chatbot-rag-ready/issues
