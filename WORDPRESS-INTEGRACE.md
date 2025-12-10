# 🤖 Integrace MATIČÁK Chatbota do WordPressu

## 📋 Přehled

Tento návod ti ukáže, jak integrovat MATIČÁK chatbota na WordPress stránku **mgo.jecool.net**.

---

## 🚀 Metoda 1: Přímá integrace (DOPORUČENO)

### Krok 1: Nahraj soubory na server

1. **Připoj se k serveru** přes FTP/SFTP (FileZilla, Cyberduck) nebo cPanel File Manager
2. **Nahraj tyto soubory** do složky `/wp-content/uploads/maticak-chatbot/`:
   - `chatbot-widget.js` (z `/web-integration/chatbot-widget.js`)
   - `logo_mgo.jpeg` (z `/app/static/logo_mgo.jpeg`)

### Krok 2: Uprav WordPress šablonu

**Způsob A: Přes Vzhled → Editor motivu**

1. Přihlaš se do WordPress administrace (`/wp-admin`)
2. Jdi na **Vzhled → Editor motivu**
3. Najdi soubor **`footer.php`** nebo **`header.php`**
4. Přidej **před** `</body>` tento kód:

```html
<!-- MATIČÁK Chatbot -->
<script src="<?php echo get_site_url(); ?>/wp-content/uploads/maticak-chatbot/chatbot-widget.js"></script>
<script>
    MaticakChatbot.init({
        apiUrl: 'http://TVOJE-IP-ADRESA:8000',  // Změň na IP adresu tvého serveru
        logoPath: '<?php echo get_site_url(); ?>/wp-content/uploads/maticak-chatbot/logo_mgo.jpeg'
    });
</script>
```

5. **Ulož změny**

---

**Způsob B: Přes plugin WPCode (bezpečnější)**

1. Nainstaluj plugin **WPCode** (zdarma)
2. Jdi na **Code Snippets → Add Snippet**
3. Vyber **Add Your Custom Code**
4. Vlož tento kód:

```html
<script src="<?php echo get_site_url(); ?>/wp-content/uploads/maticak-chatbot/chatbot-widget.js"></script>
<script>
    MaticakChatbot.init({
        apiUrl: 'http://TVOJE-IP-ADRESA:8000',
        logoPath: '<?php echo get_site_url(); ?>/wp-content/uploads/maticak-chatbot/logo_mgo.jpeg'
    });
</script>
```

5. **Location:** Footer
6. **Aktivuj snippet**

---

### Krok 3: Spusť backend server

**DŮLEŽITÉ:** Backend musí běžet, aby chatbot fungoval!

```bash
cd /Users/tomasmutina/Documents/Chatbot_skola_1
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Pro produkční nasazení použij:**
```bash
# Na serveru s nohup (běží na pozadí)
nohup python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 &

# Nebo s PM2 (lepší správa procesů)
pm2 start "python3 -m uvicorn main:app --host 0.0.0.0 --port 8000" --name maticak-api
pm2 save
pm2 startup
```

---

## 🌐 Metoda 2: Pomocí iframe (jednodušší, ale méně flexibilní)

### Nahraj chat.html na server

1. Nahraj celou složku `/app/` na server do `/wp-content/uploads/maticak-chatbot/`
2. V WordPressu přidej tento kód (stejně jako výše):

```html
<iframe 
    src="<?php echo get_site_url(); ?>/wp-content/uploads/maticak-chatbot/app/ui/chat.html" 
    style="position: fixed; bottom: 20px; right: 20px; width: 320px; height: 480px; border: none; z-index: 999999;"
    id="maticakChatbot"
></iframe>

<button 
    onclick="document.getElementById('maticakChatbot').style.display = document.getElementById('maticakChatbot').style.display === 'none' ? 'block' : 'none';"
    style="position: fixed; bottom: 20px; right: 20px; width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; font-size: 28px; cursor: pointer; z-index: 999998; box-shadow: 0 4px 20px rgba(102, 126, 234, 0.6);"
>
    💬
</button>
```

---

## 🔧 Metoda 3: Plugin (nejbezpečnější pro WordPress)

Vytvořím ti vlastní WordPress plugin:

