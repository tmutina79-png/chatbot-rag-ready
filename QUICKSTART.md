# 🚀 QUICK START - Nasazení za 10 minut

**Tento návod ti ukáže, jak rychle nasadit chatbota pro testování.**

## ⏱️ Časová náročnost: 10-15 minut

---

## 📋 Krok 1: Backend (5 min)

### 1.1 Jdi na Render.com
👉 https://render.com

### 1.2 Vytvoř účet
- Použij GitHub účet (nejrychlejší)

### 1.3 Vytvoř Web Service
1. Klikni **"New +"** → **"Web Service"**
2. Připoj tento GitHub repozitář
3. Nastav:
   - **Name:** `maticak-api` (nebo jiné jméno)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** Free

### 1.4 Deploy
1. Klikni **"Create Web Service"**
2. Počkaj 5-10 minut (první deploy trvá déle)
3. ✅ Až uvidíš "Live", zkopíruj URL

**Tvoje backend URL:** `_________________________________`

---

## ⚙️ Krok 2: Konfigurace (1 min)

### 2.1 Otevři `app/ui/config.js`

### 2.2 ZMĚŇ tuto řádku:
```javascript
const CONFIG = {
    API_BASE_URL: 'https://TVOJE-URL.onrender.com'  // ← VLOŽ SVOU URL!
};
```

**Příklad:**
```javascript
const CONFIG = {
    API_BASE_URL: 'https://maticak-api.onrender.com'
};
```

### 2.3 Ulož soubor

---

## 📤 Krok 3: GitHub (2 min)

### 3.1 Commit změny
```bash
git add .
git commit -m "Production ready"
git push origin main
```

### 3.2 Aktivuj GitHub Pages
1. Jdi na GitHub → tvůj repo → **Settings**
2. V levém menu klikni **Pages**
3. V "Build and deployment":
   - **Source:** GitHub Actions
4. Klikni **Save**

---

## ⏳ Krok 4: Počkej (2-3 min)

### 4.1 Sleduj build
- Jdi na GitHub → záložka **Actions**
- Počkaj, až build doběhne (zelená ✓)

### 4.2 Získej URL
- GitHub Pages URL: `https://TVOJE-JMENO.github.io/chatbot-rag-ready/`

**Tvoje URL:** `_________________________________`

---

## ✅ Krok 5: Otestuj (2 min)

### 5.1 Otevři URL v prohlížeči

### 5.2 Zkontroluj:
- [ ] Chatbot se zobrazil v pravém dolním rohu
- [ ] Klikni "Kontakt" → funguje
- [ ] Klikni "Jídelna" → funguje
- [ ] Menu se načítá (ne "loading" pořád)

### 5.3 F12 → Console
- [ ] Žádné červené chyby
- [ ] Žádné CORS chyby

---

## 🎉 Krok 6: Sdílej

### 6.1 Zkrať URL (volitelné)
- Jdi na https://bit.ly
- Vlož svou GitHub Pages URL
- Získej krátký odkaz

### 6.2 Pošli účastníkům
```
Ahoj! 👋

Testuj prosím nového chatbota MATIČÁK:
https://bit.ly/maticak-chatbot

Vyzkoušej všechny funkce a napiš mi zpětnou vazbu!

Děkuji! 🤖
```

---

## 🐛 Problémy?

### ❌ Backend se nenasadil
- Zkontroluj logy na Render.com
- Ověř `requirements.txt`

### ❌ Chatbot se nenačte
- Zkontroluj `config.js` - správná URL?
- Ověř GitHub Actions - build úspěšný?

### ❌ API nefunguje (CORS chyba)
- V `main.py` zkontroluj:
```python
allow_origins=[
    "https://tvoje-jmeno.github.io",
    "*"
]
```
- Recommitni a redeploy

### ❌ Scraping nefunguje
- Možná se změnila struktura stránek
- Zkontroluj konzoli prohlížeče

---

## 📚 Potřebuješ víc detailů?

- **DEPLOYMENT.md** - Kompletní návod
- **DEPLOYMENT_CHECKLIST.md** - Checklist
- **TESTING.md** - Jak testovat
- **quick_commands.sh** - Užitečné příkazy

---

## 🎯 Shrnutí

```
1. Deploy backend na Render.com (5 min)
2. Změň config.js s novou URL (1 min)
3. Push na GitHub + aktivuj Pages (2 min)
4. Počkej na build (2-3 min)
5. Otestuj (2 min)
6. Sdílej s účastníky

CELKEM: ~10-15 minut
```

---

## ✅ Checklist

- [ ] Backend nasazen na Render.com
- [ ] URL zkopírována do `config.js`
- [ ] Push na GitHub
- [ ] GitHub Pages aktivován
- [ ] Build úspěšný (zelená ✓)
- [ ] Chatbot funguje na GitHub Pages URL
- [ ] Všechny funkce otestovány
- [ ] URL sdílena s účastníky

---

**Gratulujeme! Chatbot je živý! 🎉**

Pro další pomoc otevři **DEPLOYMENT.md**.

---

**Vytvořeno pro Matiční gymnázium Ostrava** ❤️
