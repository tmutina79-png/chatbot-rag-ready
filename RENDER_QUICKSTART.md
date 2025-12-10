# ⚡ RYCHLÝ START - Render.com Deployment

## 🎯 Co získáš za 10 minut:
✅ Backend online 24/7 zdarma
✅ Plně funkční chatbot pro všechny
✅ Automatické HTTPS
✅ Automatické aktualizace

---

## 🚀 3 JEDNODUCHÉ KROKY:

### **KROK 1: Registrace (2 minuty)**

1. Otevři: **https://render.com**
2. Klikni **"Get Started for Free"**
3. Zvol **"Sign up with GitHub"**
4. Potvrď přístup k repozitářům

### **KROK 2: Vytvoř Web Service (3 minuty)**

1. Klikni **"New +"** (vpravo nahoře)
2. Vyber **"Web Service"**
3. Najdi a připoj: **`chatbot-rag-ready`**
4. Vyplň:
   ```
   Name:           maticak-backend
   Region:         Frankfurt (EU Central)
   Branch:         main
   Runtime:        Python 3
   Build Command:  pip install -r requirements.txt
   Start Command:  uvicorn main:app --host 0.0.0.0 --port $PORT
   Instance Type:  Free
   ```
5. Klikni **"Create Web Service"**

### **KROK 3: Počkej a zkopíruj URL (5 minut)**

- Render builduje backend (sleduj logy)
- Po dokončení uvidíš: **"Your service is live 🎉"**
- Zkopíruj URL nahoře (např. `https://maticak-backend.onrender.com`)

---

## ✅ Otestuj backend:

Otevři v prohlížeči:
```
https://TVOJE-URL.onrender.com/docs
```

Měl bys vidět FastAPI dokumentaci! ✨

---

## 🔧 Propoj s chatbotem:

### **Použij interaktivní script:**
```bash
./deploy_backend.sh
```

### **Nebo ručně:**

1. Uprav `docs/config.js`:
```javascript
const CONFIG = {
    API_BASE_URL: 'https://TVOJE-URL.onrender.com'
};
```

2. Commit a push:
```bash
git add docs/config.js
git commit -m "Update backend URL"
git push origin main
```

3. Počkej 1-2 minuty na GitHub Pages update

---

## 🎉 HOTOVO!

Tvůj chatbot je teď plně funkční:
```
https://tmutina79-png.github.io/chatbot-rag-ready/
```

**Testuj:**
- ✅ Kontakt
- ✅ Jídelna
- ✅ Rozvrh
- ✅ AI chat

---

## 📊 Co se stalo?

```
┌──────────────────┐
│  GitHub Pages    │  ← Frontend (chatbot UI)
│  (tmutina79...)  │
└────────┬─────────┘
         │ API calls
         ↓
┌──────────────────┐
│  Render.com      │  ← Backend (FastAPI server)
│  (maticak...)    │
└──────────────────┘
```

---

## 💡 Tipy:

### Backend je pomalý?
- Free tier spí po 15 min → první request trvá ~30s
- Řešení: Upgrade na $7/měsíc nebo použij cron-job.org pro keep-alive

### Chceš sledovat logy?
- Jdi na Render dashboard → tvůj service → Logs tab

### Vlastní doména?
- Render Settings → Custom Domain → Přidej CNAME záznam

---

## 🆘 Problémy?

**Build fails:**
- Zkontroluj `requirements.txt` - všechny balíčky jsou tam?

**CORS error:**
- Zkontroluj `main.py` - `allow_origins=["*"]` je nastaveno?

**Chatbot nefunguje:**
- Otevři F12 → Console → hledej chyby
- Zkontroluj URL v `docs/config.js`

---

## 📚 Dokumentace:
- **Detailní návod**: `RENDER_DEPLOYMENT.md`
- **GitHub Pages**: `GITHUB_PAGES_QUICKSTART.md`

---

**Teď jdi na https://render.com a nasaď! 🚀**
