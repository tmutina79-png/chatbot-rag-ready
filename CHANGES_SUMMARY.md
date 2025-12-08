# ✅ Souhrn změn pro nasazení na GitHub

## 🎯 Cíl
Připravit chatbota MATIČÁK pro nasazení na GitHub Pages a umožnit sdílení s účastníky testování.

## 📝 Provedené změny

### 1. Frontend - Konfigurace API
**Nový soubor:** `app/ui/config.js`
- Centralizovaná konfigurace API URL
- Automatická detekce prostředí (localhost vs produkce)
- Snadná změna URL pro produkční nasazení

**Upravený soubor:** `app/ui/chat.html`
- Import `config.js` v `<head>`
- Všechny `fetch()` volání používají `${CONFIG.API_BASE_URL}`
- Změněno celkem 6 endpointů:
  - `/jidelna/dnesni-menu`
  - `/jidelna/tydenni-menu`
  - `/kontakt/vedeni`
  - `/kontakt/ucitele/{id}`
  - `/chat`

**Nový soubor:** `app/ui/index.html`
- Landing page s přesměrováním na `chat.html`
- Uživatelé můžou otevřít přímo root URL

### 2. GitHub Actions
**Nový soubor:** `.github/workflows/deploy.yml`
- Automatické nasazení na GitHub Pages
- Spouští se při push na `main` branch
- Deploy trvá 2-3 minuty

### 3. Dokumentace

#### **DEPLOYMENT.md** (hlavní návod)
- Krok-za-krokem návod na nasazení
- 3 možnosti backendu (Render, Railway, PythonAnywhere)
- Konfigurace CORS
- Řešení problémů
- Alternativa: lokální síť testování

#### **DEPLOYMENT_CHECKLIST.md** (checklist)
- Checklist před nasazením
- Checklist během nasazení
- Checklist po nasazení
- Místo pro poznámky

#### **TESTING.md** (testování)
- Automatický test script
- Manuální testovací postup
- Kontrola scrapingu
- Checklist před nasazením

#### **TESTING_INSTRUCTIONS_FOR_USERS.md**
- Návod pro účastníky testování
- Co testovat
- Jak nahlásit problémy
- FAQ

#### **ENVIRONMENT_VARIABLES.md**
- Návod na env variables
- Bezpečnostní tipy

#### **USEFUL_LINKS.md**
- Odkazy na hosting platformy
- Dokumentace
- Učební materiály
- Komunity

#### **README.md** (aktualizován)
- Přehledný quick start
- Odkazy na další dokumentaci
- Stručný popis projektu

### 4. Testovací nástroje

**Nový soubor:** `test_api.py`
- Automatický test všech endpointů
- Barevný výstup v terminálu
- Použití: `python3 test_api.py`

**Nový soubor:** `start_local_testing.sh`
- Skript pro snadné spuštění lokálního testování
- Automaticky zjistí IP adresu
- Zobrazí instrukce pro účastníky
- Použití: `./start_local_testing.sh`

## 🔧 Co je potřeba udělat PŘED nasazením

### ⚠️ KRITICKÉ - MUSÍŠ ZMĚNIT:

1. **`app/ui/config.js`** - ZMĚŇ URL backendu:
   ```javascript
   const CONFIG = {
       API_BASE_URL: 'https://tvoje-backend-url.com'  // ← TADY!
   };
   ```

2. **Deploy backend** na Render.com (nebo jinou platformu)
   - Následuj návod v DEPLOYMENT.md
   - Zkopíruj URL

3. **Push na GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

4. **Aktivuj GitHub Pages**
   - Settings → Pages → Source: GitHub Actions

## 📋 Postup nasazení (rychlá verze)

```bash
# 1. Otestuj lokálně
python3 test_api.py

# 2. Deploy backend na Render.com
# (následuj DEPLOYMENT.md)

# 3. Aktualizuj config.js s novou URL

# 4. Push na GitHub
git add .
git commit -m "Production ready"
git push origin main

# 5. Aktivuj GitHub Pages v Settings

# 6. Počkej 2-3 minuty

# 7. Sdílej URL:
# https://tvoje-jmeno.github.io/chatbot-rag-ready/
```

## ✅ Co funguje po nasazení

- ✅ Chatbot widget v pravém dolním rohu
- ✅ Kontakty (vedení, učitelé)
- ✅ Jídelna (dnešní, týdenní menu)
- ✅ Chat funkce
- ✅ Typing efekt s možností přeskočení
- ✅ Responzivní design
- ✅ Automatické scrollování

## 📱 Jak sdílet s účastníky

1. Zkopíruj GitHub Pages URL
2. Zkrať pomocí bit.ly nebo tinyurl.com
3. Pošli email/zprávu s odkazem
4. Přilož TESTING_INSTRUCTIONS_FOR_USERS.md

## 🆘 Řešení problémů

### Chatbot se nenačte
→ Zkontroluj config.js, GitHub Actions log

### API nefunguje
→ Zkontroluj, že backend běží (otevři /docs)
→ Zkontroluj CORS v main.py

### Scraping vrací prázdná data
→ Stránky se mohly změnit
→ Zkontroluj HTML strukturu

## 📊 Statistiky změn

- **Nové soubory:** 11
- **Upravené soubory:** 3
- **Řádků dokumentace:** ~1000+
- **Řádků kódu:** ~100

## 🎉 Shrnutí

Chatbot je **připraven k nasazení**! 

Všechny potřebné soubory, návody a nástroje jsou vytvořeny.

**Další kroky:**
1. Přečti DEPLOYMENT.md
2. Projdi DEPLOYMENT_CHECKLIST.md
3. Nasaď backend
4. Aktualizuj config.js
5. Push a aktivuj GitHub Pages
6. Sdílej s účastníky

**Good luck! 🚀**

---

**Datum vytvoření:** 8. prosince 2025
**Autor:** GitHub Copilot + Tomáš Mutina
**Pro:** Matiční gymnázium Ostrava
