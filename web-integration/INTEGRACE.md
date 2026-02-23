# 🤖 MATY Chatbot - Integrace na webovou stránku

## 🚀 Rychlá integrace (2 řádky kódu!)

### Krok 1: Stáhni soubor
Použij tento soubor: **`chatbot-widget-v2.js`**

### Krok 2: Přidej do své stránky
Vlož tento kód **před uzavírací tag `</body>`**:

```html
<!-- MATY Chatbot -->
<script src="chatbot-widget-v2.js"></script>
<script>MaticakChatbot.init();</script>
```

**To je vše!** Chatbot bude fungovat automaticky. 🎉

---

## 📋 Kompletní příklad HTML

```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Moje webová stránka</title>
</head>
<body>
    
    <!-- Tvůj obsah stránky -->
    <h1>Vítej na mé stránce!</h1>
    <p>Nějaký obsah...</p>
    
    <!-- MATY Chatbot - přidej před </body> -->
    <script src="chatbot-widget-v2.js"></script>
    <script>MaticakChatbot.init();</script>
</body>
</html>
```

---

## 🎯 Funkce chatbota

✅ **Plně funkční** - Kontakt, Jídelna, Rozvrh, AI odpovědi  
✅ **Plovoucí tlačítko** 💬 - Vždy v pravém dolním rohu  
✅ **Responzivní** - Funguje na mobilu i počítači  
✅ **Žádná konfigurace** - Funguje hned po vložení  
✅ **Nulový dopad** - Neovlivňuje výkon stránky  
✅ **Moderní design** - Kulaté rohy, gradienty, animace  

---

## 🔧 Pokročilá konfigurace (volitelné)

### Změna pozice tlačítka

```javascript
MaticakChatbot.init({
    position: {
        bottom: '50px',  // Změň vertikální pozici
        right: '50px'    // Změň horizontální pozici
    }
});
```

### Změna velikosti chatbota

```javascript
MaticakChatbot.init({
    width: '500px',   // Šířka chatbota
    height: '700px'   // Výška chatbota
});
```

### Vlastní URL chatbota (pokud máš vlastní server)

```javascript
MaticakChatbot.init({
    chatbotUrl: 'https://tvoje-domena.cz/chat.html'
});
```

---

## 🌐 Integrace na různé platformy

### WordPress

1. **Nahraj soubor:**
   - FTP: nahraj do `/wp-content/themes/tvuj-motiv/js/`
   - Nebo přes administraci: Vzhled → Editor motivů

2. **Přidej do `footer.php`** (před `</body>`):
   ```php
   <!-- MATY Chatbot -->
   <script src="<?php echo get_template_directory_uri(); ?>/js/chatbot-widget-v2.js"></script>
   <script>MaticakChatbot.init();</script>
   ```

### Statické HTML stránky

Zkopíruj `chatbot-widget-v2.js` do stejné složky jako tvoje HTML a přidej:

```html
<script src="./chatbot-widget-v2.js"></script>
<script>MaticakChatbot.init();</script>
```

### Wix, Webnode, Weebly

1. Nahraj `chatbot-widget-v2.js` někam online (např. GitHub Pages)
2. V nastavení stránky přidej Custom HTML/Code:
   ```html
   <script src="https://tvoje-url/chatbot-widget-v2.js"></script>
   <script>MaticakChatbot.init();</script>
   ```

---

## 📱 Responzivní design

Chatbot se automaticky přizpůsobí:

- **Desktop (>768px):** 400×600px widget v pravém dolním rohu
- **Tablet (≤768px):** 90% šířky, 70vh výška, zaoblené rohy nahoře
- **Mobil (≤480px):** 90% šířky, 75vh výška

---

## 🔥 Live demo

Otestuj si chatbot na:
- **GitHub Pages:** https://tmutina79-png.github.io/chatbot-rag-ready/
- **Demo stránka:** Otevři `demo.html` v prohlížeči

---

## ❓ Časté otázky

### Jak otevřít chatbot programově?
```javascript
MaticakChatbot.open();   // Otevřít
MaticakChatbot.close();  // Zavřít
MaticakChatbot.toggle(); // Přepnout
```

### Funguje to i bez internetového připojení?
Ne, chatbot potřebuje být připojený k API serveru na Render.com pro AI odpovědi.

### Ovlivní to rychlost mé stránky?
Ne! Chatbot se načítá asynchronně v iframe, taktakže neblokuje načítání stránky.

### Mohu změnit barvy/design?
Ano, ale musíš upravit CSS přímo v souboru `chat.html` (pokročilé).

---

## 📞 Podpora

Máš problém s integrací? Kontaktuj nás:
- 📧 Email: info@mgo.cz
- 🌐 Web: https://mgo.cz

---

**Vytvořili žáci Matičního gymnázia Ostrava** 🎓
