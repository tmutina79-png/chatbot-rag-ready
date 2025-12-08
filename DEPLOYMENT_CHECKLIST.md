# 📋 Checklist pro nasazení

## ☑️ Před nasazením

- [ ] Backend kód je funkční lokálně
- [ ] Frontend funguje s lokálním backendem
- [ ] Všechny funkce otestovány:
  - [ ] Tlačítko Kontakt
  - [ ] Tlačítko Jídelna
  - [ ] Vedení školy
  - [ ] Učitelé (všechny předměty)
  - [ ] Dnešní menu
  - [ ] Týdenní menu
  - [ ] Chatovací funkce

## 🌐 Nasazení backendu

### Render.com (DOPORUČENO)

- [ ] Vytvořen účet na render.com
- [ ] Vytvořen nový Web Service
- [ ] Nahrán kód nebo připojen GitHub
- [ ] Nastaveny environment variables (pokud potřeba)
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Počkáno na první deploy (5-10 min)
- [ ] Otestován endpoint: `https://tvoje-url.onrender.com/docs`
- [ ] Zkopírována URL backendu: `____________________`

## ⚙️ Konfigurace frontendu

- [ ] Otevřen soubor `app/ui/config.js`
- [ ] Změněna URL z `http://127.0.0.1:8000` na produkční URL
- [ ] Příklad:
  ```javascript
  const CONFIG = {
      API_BASE_URL: 'https://maticak-api.onrender.com'
  };
  ```
- [ ] Soubor uložen

## 📤 Push na GitHub

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

- [ ] Veškeré změny commitnuty
- [ ] Pushnuty na GitHub
- [ ] Ověřeno na GitHubu, že soubory jsou tam

## 🚀 GitHub Pages

- [ ] Otevřeny Settings repozitáře
- [ ] Kliknuto na Pages v levém menu
- [ ] V "Build and deployment":
  - Source: **GitHub Actions**
- [ ] Počkáno 2-3 minuty na build
- [ ] Otevřena záložka "Actions" - ověřen úspěšný build
- [ ] GitHub Pages URL: `____________________`

## 🔍 Testování

### Backend
- [ ] Otevřena URL: `https://tvoje-backend.com/docs`
- [ ] API Swagger UI se načetlo
- [ ] Otestován endpoint `/kontakt/vedeni`
- [ ] Otestován endpoint `/jidelna/dnesni-menu`

### Frontend
- [ ] Otevřena GitHub Pages URL
- [ ] Chatbot se zobrazil v pravém dolním rohu
- [ ] Uvítací zpráva se načetla
- [ ] Tlačítka Kontakt a Jídelna fungují
- [ ] Data se načítají z API (ne "loading" chyby)
- [ ] Otestovány všechny funkce

### Konzole prohlížeče (F12)
- [ ] Žádné červené chyby
- [ ] Žádné CORS chyby
- [ ] Network záložka ukazuje úspěšné požadavky (200)

## 📱 Sdílení s účastníky

- [ ] Vytvořen zkrácený odkaz (bit.ly nebo tinyurl.com)
- [ ] Odeslán email/zpráva s odkazem
- [ ] Přiloženy instrukce:
  ```
  Ahoj! 👋
  
  Testuj prosím nového chatbota MATIČÁK:
  https://your-url.github.io/chatbot-rag-ready/
  
  Vyzkoušej:
  ✅ Tlačítko "Kontakt" - zobraz vedení a učitele
  ✅ Tlačítko "Jídelna" - zobraz dnešní a týdenní menu
  ✅ Chatovací funkci - napiš zprávu
  
  Napiš mi prosím:
  - Co funguje ✅
  - Co nefunguje ❌
  - Návrhy na zlepšení 💡
  
  Děkuji!
  ```

## 🐛 Řešení problémů

### Chatbot se nenačte
- [ ] Zkontrolována konzole prohlížeče (F12)
- [ ] Ověřena URL v `config.js`
- [ ] Zkontrolován GitHub Actions build

### API nefunguje
- [ ] Backend běží - otevřena `/docs` URL
- [ ] Zkontrolovány logy na Render.com
- [ ] Ověřeno CORS nastavení v `main.py`

### CORS chyba
- [ ] V `main.py` přidána GitHub Pages URL:
  ```python
  allow_origins=[
      "https://tvoje-jmeno.github.io",
      "*"
  ]
  ```
- [ ] Recommitnuty změny a redeploy

## ✅ Hotovo!

- [ ] Vše funguje
- [ ] Účastníci mají přístup
- [ ] Zpětná vazba sbírána

---

**🎉 Gratulujeme k úspěšnému nasazení!**

**Poznámky:**
```
(zde si piš poznámky během procesu)




```

**Problémy a řešení:**
```
(zde si zaznamenej případné problémy a jak jsi je vyřešil)




```
