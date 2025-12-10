# 🤖 MATIČÁK Chatbot - Integrace na webovou stránku

## 📋 Obsah balíčku

Tento balíček obsahuje vše potřebné pro integraci MATIČÁK chatbota na jakoukoli webovou stránku:

```
web-integration/
├── chatbot-widget.js       # Hlavní JavaScript soubor chatbota
├── demo.html              # Demo stránka s příklady použití
└── README.md              # Tento soubor
```

## 🚀 Rychlý start

### 1. Základní integrace (2 řádky kódu)

Přidej tyto řádky **před uzavírací tag `</body>`** na tvé webové stránce:

```html
<!-- MATIČÁK Chatbot -->
<script src="chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'http://127.0.0.1:8000'
  });
</script>
```

### 2. Konfigurace API URL

Pro **produkční nasazení** změň `apiUrl` na adresu tvého serveru:

```javascript
MaticakChatbot.init({
  apiUrl: 'https://api.tvoje-domena.cz'  // Tvoje API adresa
});
```

## 🎯 Funkce chatbota

✅ **Plovoucí tlačítko** - Vždy dostupné v pravém dolním rohu
✅ **Responzivní design** - Automaticky se přizpůsobí mobilu i počítači
✅ **Rychlé akce** - Kontakt, Jídelna, Rozvrh na jedno kliknutí
✅ **Modální okna** - Přehledné zobrazení informací
✅ **API integrace** - Automatické načítání dat ze serveru
✅ **Nulový dopad** - Neovlivňuje výkon tvé stránky

## 📱 Příklad použití na mgo.jecool.net

### Pro WordPress:

1. **Nahraj soubor:**
   - Přihlaš se do administrace WordPress
   - Jdi do: Vzhled → Editor motivů → Vybrat soubor
   - Nebo nahraj přes FTP do složky: `/wp-content/themes/tvuj-motiv/js/`

2. **Přidej do footer.php:**
   ```php
   <?php wp_footer(); ?>
   
   <!-- MATIČÁK Chatbot -->
   <script src="<?php echo get_template_directory_uri(); ?>/js/chatbot-widget.js"></script>
   <script>
     MaticakChatbot.init({
       apiUrl: 'http://127.0.0.1:8000'
     });
   </script>
   
   </body>
   </html>
   ```

### Pro statické HTML stránky:

Přidej před `</body>`:

```html
<!-- MATIČÁK Chatbot -->
<script src="./chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'http://127.0.0.1:8000'
  });
</script>
```

## 🛠️ Pokročilá konfigurace

### Změna pozice plovoucího tlačítka

Edituj v `chatbot-widget.js` řádek s `#maticak-chat-toggle-btn`:

```css
#maticak-chat-toggle-btn {
    position: fixed;
    bottom: 20px;    /* Změň pro jinou pozici */
    right: 20px;     /* Změň pro jinou pozici */
    /* ... */
}
```

### Změna barev

Najdi v `chatbot-widget.js` gradient barvy:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Změň hexadecimální kódy na tvé barvy, např.:
```css
background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
```

### Změna velikosti chatbota

V `chatbot-widget.js` najdi `#maticak-chatbot-container`:

```css
#maticak-chatbot-container {
    width: 320px;    /* Změň šířku */
    height: 480px;   /* Změň výšku */
    /* ... */
}
```

### Změna Z-indexu (vrstvy)

Pokud je chatbot skrytý za jinými prvky, zvyš z-index:

```javascript
config: {
    apiUrl: window.location.origin,
    containerZIndex: 999999,    // Zvyš toto číslo
    buttonZIndex: 999998        // Zvyš toto číslo
}
```

## 🎨 Styly a vzhled

Chatbot používá **vlastní izolované styly**, které neovlivní tvou stránku:
- Všechny třídy začínají prefixem `maticak-`
- Žádné globální CSS konflikty
- Responzivní na všech zařízeních

## 📊 Testování

### Lokální test:

1. **Spusť FastAPI server:**
   ```bash
   cd /Users/tomasmutina/Documents/Chatbot_skola_1
   python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Otevři demo.html v prohlížeči:**
   ```bash
   open web-integration/demo.html
   ```

3. **Klikni na plovoucí tlačítko 💬** v pravém dolním rohu

### Test na živé stránce:

1. Nahraj `chatbot-widget.js` na tvůj webhosting
2. Přidej integrační kód do HTML
3. Otevři stránku v prohlížeči
4. Mělo by se zobrazit plovoucí tlačítko 💬

## 🔧 Řešení problémů

### Chatbot se nezobrazuje

✅ **Zkontroluj konzoli prohlížeče** (F12 → Console)
✅ **Ověř cestu k souboru** - Musí být správná relativní/absolutní cesta
✅ **Zkontroluj z-index** - Možná je skrytý za jiným prvkem

### API nefunguje

✅ **Server běží?** - Zkontroluj `ps aux | grep uvicorn`
✅ **Správná URL?** - Zkontroluj `apiUrl` v konfiguraci
✅ **CORS?** - FastAPI musí povolit CORS pro tvou doménu

### Chatbot překrývá obsah

✅ **Změň pozici** - Edituj `bottom` a `right` v CSS
✅ **Zmenši velikost** - Upravy `width` a `height`
✅ **Responzivní breakpointy** - Přidej media queries

## 📞 Podpora

**Vytvořeno:** Žáci Matičního gymnázia Ostrava
**Kontakt:** info@mgo.cz
**Web:** https://mgo.cz

## 📄 Licence

Tento chatbot je vytvořen pro potřeby Matičního gymnázia Ostrava.

## 🔄 Aktualizace

Pro aktualizaci chatbota:
1. Stáhni novou verzi `chatbot-widget.js`
2. Nahraď starý soubor na serveru
3. Vymaž cache prohlížeče (Ctrl+F5)

## 🎓 Další kroky

1. ✅ Otestuj demo.html lokálně
2. ✅ Nahraj chatbot-widget.js na tvůj server
3. ✅ Přidej integrační kód do HTML
4. ✅ Nastav správnou API URL
5. ✅ Otestuj na živé stránce
6. ✅ Přizpůsob barvy a pozici (volitelné)

---

**Happy coding! 🚀**
