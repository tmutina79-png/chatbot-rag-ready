# 🚀 Nasazení Chatbota MATIČÁK

## Postup nasazení na GitHub Pages

### 1️⃣ Příprava backendu

Backend musí běžet na veřejně přístupném serveru. Máš několik možností:

#### Možnost A: Render.com (DOPORUČENO - ZDARMA)
1. Jdi na [render.com](https://render.com)
2. Vytvoř účet
3. Klikni na "New" → "Web Service"
4. Připoj GitHub repo nebo nahraj kód
5. Nastav:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Počkej na deploy (5-10 min)
7. Zkopíruj URL (např. `https://maticak-api.onrender.com`)

#### Možnost B: Railway.app (ZDARMA)
1. Jdi na [railway.app](https://railway.app)
2. Vytvoř projekt
3. Připoj GitHub repo
4. Railway automaticky detekuje Python a spustí server
5. Zkopíruj URL

#### Možnost C: PythonAnywhere (ZDARMA s limity)
1. Vytvoř účet na [pythonanywhere.com](https://www.pythonanywhere.com)
2. Nahraj soubory
3. Nastav WSGI konfiguraci
4. Zkopíruj URL

### 2️⃣ Aktualizace konfigurace

Po nasazení backendu **MUSÍŠ** upravit `app/ui/config.js`:

```javascript
const CONFIG = {
    API_BASE_URL: 'https://tvoje-backend-url.com'  // ← ZMĚŇ TUTO URL!
};
```

**Příklad:**
```javascript
const CONFIG = {
    API_BASE_URL: 'https://maticak-api.onrender.com'
};
```

### 3️⃣ Nasazení frontendu na GitHub Pages

#### Krok 1: Push do GitHubu
```bash
git add .
git commit -m "Připraveno pro deployment"
git push origin main
```

#### Krok 2: Aktivuj GitHub Pages
1. Jdi na GitHub → tvoje repo → **Settings**
2. V levém menu klikni na **Pages**
3. V sekci "Build and deployment":
   - **Source**: GitHub Actions
4. Počkej 2-3 minuty na build

#### Krok 3: Získej URL
- GitHub Pages URL bude: `https://tvoje-uzivatelske-jmeno.github.io/chatbot-rag-ready/chat.html`
- Nebo pokud máš vlastní doménu, nastav ji v Settings → Pages

### 4️⃣ CORS nastavení

Backend MUSÍ povolit přístup z GitHub Pages. V `main.py` zkontroluj:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:8000",
        "https://tvoje-uzivatelske-jmeno.github.io",  # ← PŘIDEJ SVOU GITHUB PAGES URL
        "*"  # Nebo povolit všechny (méně bezpečné)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 5️⃣ Testování

1. Otevři GitHub Pages URL v prohlížeči
2. Chatbot by se měl načíst v pravém dolním rohu
3. Vyzkoušej:
   - ✅ Tlačítko "Kontakt"
   - ✅ Tlačítko "Jídelna"
   - ✅ Týdenní menu
   - ✅ Vedení školy
   - ✅ Učitelé
   - ✅ Chatovací funkce

### 🐛 Řešení problémů

#### Chatbot se nenačte
- Zkontroluj konzoli prohlížeče (F12)
- Ověř URL v `config.js`

#### API nefunguje
- Zkontroluj, že backend běží: otevři `https://tvoje-backend-url.com/docs`
- Ověř CORS nastavení
- Zkontroluj logy na serveru (Render/Railway)

#### 404 chyba na GitHub Pages
- Ujisti se, že GitHub Actions workflow běžel úspěšně
- Zkontroluj záložku "Actions" v repozitáři
- URL musí obsahovat `/chat.html` na konci

### 📝 Sdílení s účastníky

Když vše funguje, sdílej tuto URL:
```
https://tvoje-uzivatelske-jmeno.github.io/chatbot-rag-ready/chat.html
```

**Nebo vytvoř krátký odkaz:**
- Použij [bit.ly](https://bit.ly)
- Nebo [tinyurl.com](https://tinyurl.com)

### 🔄 Aktualizace

Když změníš kód:
```bash
git add .
git commit -m "Popis změny"
git push origin main
```

GitHub Actions automaticky nasadí novou verzi (2-3 minuty).

---

## ⚙️ Alternativa: Lokální testování před nasazením

Pro testování s účastníky ve stejné síti:

1. Zjisti svou IP adresu:
   ```bash
   # macOS/Linux
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

2. Spusť server s externí IP:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. V `config.js` nastav:
   ```javascript
   API_BASE_URL: 'http://TVOJE-IP:8000'
   ```

4. Otevři `chat.html` přímo v prohlížeči nebo pomocí:
   ```bash
   python3 -m http.server 3000
   ```

5. Účastníci zadají v prohlížeči:
   ```
   http://TVOJE-IP:3000/app/ui/chat.html
   ```

**⚠️ POZOR:** Toto funguje jen ve stejné WiFi síti!

---

## 📧 Potřebuješ pomoc?

Pokud něco nefunguje, zkontroluj:
1. ✅ Backend běží a je přístupný
2. ✅ URL v `config.js` je správná
3. ✅ CORS je správně nastavený
4. ✅ GitHub Pages je aktivovaný
5. ✅ Konzole prohlížeče (F12) nehlásí chyby

---

**Úspěšné nasazení! 🎉**
