# 🤖 MATIČÁK Chatbot - WordPress Plugin

## 📦 Instalace pluginu

### Krok 1: Příprava souborů

1. **Vytvoř ZIP archiv** obsahující:
   ```
   maticak-chatbot/
   ├── maticak-chatbot.php
   └── README.md
   ```

2. Nebo zkopíruj celou složku `wordpress-plugin/` na server do:
   ```
   /wp-content/plugins/maticak-chatbot/
   ```

### Krok 2: Instalace do WordPressu

**Způsob A: Přes WordPress admin (doporučeno)**

1. Přihlaš se do WordPress administrace
2. Jdi na **Pluginy → Přidat nový**
3. Klikni na **Nahrát plugin**
4. Vyber ZIP soubor s pluginem
5. Klikni **Instalovat**
6. **Aktivuj** plugin

**Způsob B: Přes FTP/SFTP**

1. Nahraj složku `maticak-chatbot/` do `/wp-content/plugins/`
2. V WordPress admin jdi na **Pluginy**
3. Najdi "MATIČÁK Chatbot" a aktivuj ho

### Krok 3: Nahraj soubory chatbota

Nahraj tyto soubory na server do `/wp-content/uploads/maticak-chatbot/`:

- `chatbot-widget.js` (z `/web-integration/chatbot-widget.js`)
- `logo_mgo.jpeg` (z `/app/static/logo_mgo.jpeg`)

**Přes FTP:**
```
/wp-content/uploads/maticak-chatbot/
├── chatbot-widget.js
└── logo_mgo.jpeg
```

**Přes cPanel File Manager:**
1. Otevři File Manager
2. Najdi složku `public_html/wp-content/uploads/`
3. Vytvoř novou složku `maticak-chatbot`
4. Nahraj do ní oba soubory

### Krok 4: Konfigurace

1. V WordPress admin jdi na **Nastavení → MATIČÁK Chatbot**
2. Nastav **API URL** (např. `http://192.168.1.100:8000` nebo `http://tvuj-server.cz:8000`)
3. Zaškrtni **Povolit chatbot**
4. Klikni **Uložit změny**
5. Otestuj připojení pomocí tlačítka **Otestovat připojení k API**

### Krok 5: Spusť backend server

**Na tvém počítači/serveru:**

```bash
cd /Users/tomasmutina/Documents/Chatbot_skola_1
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Pro produkční nasazení (server běží neustále):**

```bash
# Pomocí nohup
nohup python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 > chatbot.log 2>&1 &

# Nebo pomocí screen
screen -S maticak-bot
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
# Stiskni Ctrl+A, pak D pro odpojení

# Nebo pomocí PM2 (nejlepší)
npm install -g pm2
pm2 start "python3 -m uvicorn main:app --host 0.0.0.0 --port 8000" --name maticak-api
pm2 save
pm2 startup
```

---

## ⚙️ Konfigurace API URL

### Lokální vývoj
```
http://127.0.0.1:8000
```

### Server v lokální síti
```
http://192.168.1.XXX:8000  (zjisti IP přes `ifconfig` nebo `ip addr`)
```

### Veřejný server
```
http://tvuj-server.cz:8000
```

### S reverse proxy (NGINX/Apache) - DOPORUČENO PRO PRODUKCI
```
https://mgo.jecool.net/api
```

---

## 🔧 Pokročilá konfigurace

### NGINX reverse proxy (doporučeno pro produkci)

Přidej do NGINX konfigurace:

```nginx
server {
    listen 80;
    server_name mgo.jecool.net;

    # WordPress
    location / {
        # Tvá běžná WordPress konfigurace
    }

    # Chatbot API
    location /api/ {
        proxy_pass http://127.0.0.1:8000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Pak nastav API URL v pluginu na: `https://mgo.jecool.net/api`

### Apache reverse proxy

V `.htaccess` nebo VirtualHost:

```apache
<Location /api>
    ProxyPass http://127.0.0.1:8000
    ProxyPassReverse http://127.0.0.1:8000
</Location>
```

---

## 🧪 Testování

### 1. Test zda běží backend
```bash
curl http://TVOJE-IP:8000/jidelna/dnesni-menu
```

### 2. Test v prohlížeči
Otevři: `http://mgo.jecool.net` a chatbot by se měl objevit vpravo dole.

### 3. Test v admin konzoli
V nastavení pluginu klikni na **Otestovat připojení k API**

---

## 🐛 Řešení problémů

### Chatbot se nezobrazuje
1. ✅ Zkontroluj, že je plugin aktivován
2. ✅ Zkontroluj nastavení "Povolit chatbot"
3. ✅ Otevři konzoli prohlížeče (F12) a zkontroluj chyby
4. ✅ Zkontroluj, že existují soubory v `/wp-content/uploads/maticak-chatbot/`

### Chatbot nefunguje (nezobrazuje data)
1. ✅ Zkontroluj, že backend běží: `curl http://TVOJE-IP:8000/jidelna/dnesni-menu`
2. ✅ Zkontroluj API URL v nastavení pluginu
3. ✅ Zkontroluj firewall - port 8000 musí být otevřený
4. ✅ Zkontroluj CORS - v `main.py` musí být správná konfigurace

### CORS Error
Upravit `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://mgo.jecool.net", "https://mgo.jecool.net"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📱 Mobilní optimalizace

Chatbot je plně responzivní a funguje na:
- ✅ Desktop (1920px+)
- ✅ Tablet landscape (1024px)
- ✅ Tablet portrait (768px)
- ✅ Mobil velký (480px)
- ✅ Mobil malý (360px)

---

## 🎨 Přizpůsobení designu

Pokud chceš změnit barvy, edituj `chatbot-widget.js` a nahraj novou verzi:

```javascript
// Najdi v souboru gradient barvy:
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

// Změň na vlastní barvy (např. zelená):
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
```

---

## 📞 Podpora

Pokud máš problémy, zkontroluj:
1. Server logs: `tail -f chatbot.log`
2. WordPress debug: V `wp-config.php` nastav `define('WP_DEBUG', true);`
3. Browser console (F12)

---

## 📄 Licence

GPL v2 or later

Vytvořili žáci Matičního gymnázia Ostrava
