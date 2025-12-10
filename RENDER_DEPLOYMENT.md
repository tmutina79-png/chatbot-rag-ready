# 🚀 RENDER.COM DEPLOYMENT - KROK ZA KROKEM

## ✅ Proč Render.com?
- ✅ **ZDARMA** (Free tier)
- ✅ Automatický deployment z GitHubu
- ✅ SSL certifikát zdarma
- ✅ Snadná konfigurace

---

## 📋 POSTUP (10 minut)

### **KROK 1: Vytvoř účet na Render.com**

1. Jdi na: **https://render.com**
2. Klikni **"Get Started for Free"**
3. Zaregistruj se pomocí **GitHub účtu** (doporučeno)
4. Potvrď email

---

### **KROK 2: Vytvoř nový Web Service**

1. Po přihlášení klikni na **"New +"** (vpravo nahoře)
2. Vyber **"Web Service"**
3. Připoj GitHub:
   - Klikni **"Connect GitHub"**
   - Autorizuj Render přístup k repozitářům
   - Najdi a vyber repository: **`chatbot-rag-ready`**

---

### **KROK 3: Nastav konfiguraci**

Vyplň formulář:

```
Name:               maticak-backend
Region:             Frankfurt (EU Central)
Branch:             main
Runtime:            Python 3
Build Command:      pip install -r requirements.txt
Start Command:      uvicorn main:app --host 0.0.0.0 --port $PORT
Instance Type:      Free
```

**Důležité nastavení:**
- ✅ **Auto-Deploy**: ANO (automatický deploy při push)
- ✅ **Environment Variables**: Zatím necháme prázdné

---

### **KROK 4: Klikni "Create Web Service"**

- Render začne buildovat tvůj backend
- Trvá to **5-10 minut** (první build)
- Uvidíš log s progress
- Počkej na: **"Your service is live 🎉"**

---

### **KROK 5: Zkopíruj URL backendu**

Po úspěšném deployi uvidíš URL nahoře:

```
https://maticak-backend.onrender.com
```

**Zkopíruj si tuto URL!** Budeš ji potřebovat v dalším kroku.

---

### **KROK 6: Otestuj backend**

Otevři v prohlížeči:
```
https://maticak-backend.onrender.com/docs
```

Měl bys vidět FastAPI dokumentaci! ✅

Vyzkoušej i:
```
https://maticak-backend.onrender.com/kontakt/vedeni
https://maticak-backend.onrender.com/jidelna/dnesni-menu
```

---

### **KROK 7: Aktualizuj config.js pro GitHub Pages**

1. Otevři soubor: `docs/config.js`
2. Změň API URL:

```javascript
const CONFIG = {
    API_BASE_URL: 'https://maticak-backend.onrender.com'  // ← TVOJE URL Z KROKU 5
};
```

3. Ulož soubor

---

### **KROK 8: Commitni a pushni změny**

```bash
cd /Users/tomasmutina/Documents/Chatbot_skola_1

# Zkopíruj aktualizovaný config.js
cp app/ui/config.js docs/config.js

# Commit
git add docs/config.js
git commit -m "Update API URL for production (Render.com)"
git push origin main
```

---

### **KROK 9: Počkej 1-2 minuty**

GitHub Pages se automaticky aktualizuje po push.

---

### **KROK 10: Otevři chatbot a testuj! 🎉**

```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

**Vyzkoušej:**
- ✅ Kontakt → Vedení školy
- ✅ Kontakt → Učitelé
- ✅ Jídelna → Dnešní menu
- ✅ Rozvrh → Třída KVA
- ✅ AI chat

---

## 🐛 Řešení problémů

### Backend se nespustí
**Chyba v logu:** `ModuleNotFoundError`
- Zkontroluj `requirements.txt` - všechny balíčky jsou tam?
- Přidej chybějící balíčky

**Port error:**
- Start command MUSÍ obsahovat `--port $PORT` (s $ dolarem!)

### CORS error v prohlížeči
**Chyba:** `Access-Control-Allow-Origin`
- Zkontroluj `main.py` - CORS middleware je správně nastavený?
- Mělo by tam být: `allow_origins=["*"]`

### Backend je pomalý (Free tier)
- Render.com uspává free služby po 15 min neaktivity
- První request po probuzení trvá ~30 sekund
- Řešení: Upgrade na placený plán ($7/měsíc) nebo použij jiný hosting

### Chatbot nefunguje
1. Zkontroluj backend URL v `docs/config.js`
2. Otevři Developer Console (F12) → záložka Console
3. Hledej chyby (červené zprávy)
4. Zkontroluj Network tab - volají se API endpointy?

---

## 💡 Tipy pro optimalizaci

### Aby backend "nespal"
Vytvoř cron job, který každých 10 minut pingnute backend:
```
https://cron-job.org/en/
```

### Monitoring
- Render dashboard ukazuje logy a metriky
- Sleduj chyby a výkon

### Custom doména
V Render Settings → Custom Domain:
```
api.maticak.cz → maticak-backend.onrender.com
```

---

## 📊 Po nasazení

### Co se stalo:
✅ Backend běží na: `https://maticak-backend.onrender.com`
✅ Frontend běží na: `https://tmutina79-png.github.io/chatbot-rag-ready/`
✅ Chatbot je plně funkční a online!

### Sdílení:
Pošli lidem tuto URL:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

---

## 🔄 Aktualizace v budoucnu

Když změníš kód:

```bash
# 1. Commitni změny
git add .
git commit -m "Update chatbot"
git push origin main

# 2. Render automaticky znovu nasadí backend (5 min)
# 3. GitHub Pages automaticky aktualizuje frontend (1-2 min)

# 4. Hotovo! Změny jsou online
```

---

## 📞 Další kroky

- [ ] Nasadit backend na Render.com
- [ ] Aktualizovat config.js s produkční URL
- [ ] Otestovat všechny funkce
- [ ] Sdílet URL se studenty/učiteli
- [ ] (Volitelně) Nastavit vlastní doménu

---

**Teď jdi na https://render.com a začni! 🚀**
