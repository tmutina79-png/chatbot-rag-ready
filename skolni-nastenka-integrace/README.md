# 🎓 MATIČÁK Chatbot - Integrace pro skolni-nastenka.cz

## 📦 Balíček pro integraci

Tento balíček obsahuje vše potřebné pro napojení MATIČÁK chatbota na web **skolni-nastenka.cz**.

---

## 📋 Co je v balíčku

```
skolni-nastenka-integrace/
├── chatbot-widget.js          # Hlavní JavaScript soubor chatbota
├── priklad-integrace.html     # Ukázkový příklad použití
└── README.md                  # Tento soubor s instrukcemi
```

---

## 🚀 Rychlý postup integrace (3 kroky)

### **KROK 1: Nahraj soubor na server**

Nahraj soubor `chatbot-widget.js` na server **skolni-nastenka.cz**.

**Doporučené umístění:**
- `/js/chatbot-widget.js`
- `/assets/js/chatbot-widget.js`
- Nebo jiná složka podle struktury webu

---

### **KROK 2: Přidej kód do HTML**

Otevři soubor, kde chceš chatbot zobrazit (např. `footer.php`, `index.html` nebo šablonu webu) a **před uzavírací tag `</body>`** přidej:

```html
<!-- MATIČÁK Chatbot -->
<script src="/js/chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'https://deploy-web-service-enfc.onrender.com'
  });
</script>
</body>
</html>
```

**Poznámka:** Pokud máš chatbot na vlastním serveru, změň `apiUrl` na svou adresu.

---

### **KROK 3: Otestuj**

1. Otevři stránku v prohlížeči
2. Mělo by se objevit **plovoucí tlačítko** 💬 v pravém dolním rohu
3. Po kliknutí se otevře chatbot s rychlými akcemi

---

## ✨ Co chatbot umí

✅ **Kontaktní informace** - E-mail, telefon, webové stránky  
✅ **Dnešní jídelníček** - Automaticky načítá menu z API  
✅ **Rozvrh hodin** - (ve vývoji)  
✅ **Responzivní design** - Automaticky se přizpůsobí mobilu i počítači  
✅ **Plovoucí tlačítko** - Vždy přístupné, neruší obsah stránky  

---

## 🛠️ Pokročilé možnosti

### Změna API serveru

Pokud máš chatbot nasazený na vlastním serveru, změň `apiUrl`:

```javascript
MaticakChatbot.init({
  apiUrl: 'https://tvoje-server-adresa.cz'
});
```

### Změna pozice tlačítka

Edituj v souboru `chatbot-widget.js` řádek s `#maticak-chat-toggle-btn`:

```css
#maticak-chat-toggle-btn {
    position: fixed;
    bottom: 20px;    /* Změň vertikální pozici */
    right: 20px;     /* Změň horizontální pozici */
    /* ... */
}
```

### Změna barev

V souboru `chatbot-widget.js` najdi sekci se styly a změň barevné gradienty:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

---

## 📱 Integrace podle typu webu

### **Pro WordPress:**

1. Přihlaš se do administrace WordPress
2. Jdi do: **Vzhled → Editor motivů**
3. Najdi soubor `footer.php` nebo `header.php`
4. Přidej kód **před `</body>`**:

```php
<?php wp_footer(); ?>

<!-- MATIČÁK Chatbot -->
<script src="<?php echo get_template_directory_uri(); ?>/js/chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'https://deploy-web-service-enfc.onrender.com'
  });
</script>

</body>
</html>
```

### **Pro statické HTML stránky:**

Přidej před `</body>` na každé stránce, kde chceš chatbot:

```html
<!-- MATIČÁK Chatbot -->
<script src="./js/chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'https://deploy-web-service-enfc.onrender.com'
  });
</script>
```

### **Pro PHP stránky:**

Vytvoř soubor `chatbot-init.php`:

```php
<!-- MATIČÁK Chatbot -->
<script src="/js/chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'https://deploy-web-service-enfc.onrender.com'
  });
</script>
```

A pak ho include na konci každé stránky:

```php
<?php include 'chatbot-init.php'; ?>
</body>
</html>
```

---

## 🧪 Testování

### Lokální testování před nahráním na server:

1. Otevři soubor `priklad-integrace.html` v prohlížeči
2. Chatbot by měl fungovat okamžitě
3. Vyzkoušej tlačítka: Kontakt, Jídelna

### Kontrolní checklist po integraci:

- [ ] Plovoucí tlačítko 💬 je viditelné v pravém dolním rohu
- [ ] Po kliknutí se chatbot otevře
- [ ] Tlačítka "Kontakt", "Jídelna" fungují
- [ ] Chatbot se správně zobrazuje na mobilu
- [ ] Neruší ostatní obsah stránky

---

## 🐛 Řešení problémů

### Chatbot se nezobrazuje

1. **Zkontroluj cestu k souboru** - Ujisti se, že `src="/js/chatbot-widget.js"` odpovídá skutečnému umístění
2. **Otevři konzoli prohlížeče** (F12) - Hledej chybové hlášky
3. **Zkontroluj, že skript je před `</body>`**

### API nefunguje

1. **Zkontroluj API URL** - Ujisti se, že adresa serveru je správná
2. **Otevři konzoli prohlížeče** - Hledej chyby síťových požadavků
3. **Test API** - Otevři v prohlížeči: `https://deploy-web-service-enfc.onrender.com/jidelna/dnesni-menu`

### Chatbot ruší design stránky

Chatbot používá vysokou hodnotu `z-index: 999999`, takže by měl být vždy nahoře. Pokud máš problémy:

1. Edituj v `chatbot-widget.js` hodnotu `containerZIndex`
2. Nebo změň `position: fixed` na jinou pozici

---

## 📞 Podpora

Pro technickou podporu nebo dotazy kontaktujte:
- **E-mail:** info@mgo.cz
- **GitHub:** [github.com/maticni-gympl/chatbot](https://github.com/maticni-gympl/chatbot)

---

## 📄 Licence

Vytvořili žáci Matičního gymnázia Ostrava © 2026

---

**Hotovo! 🎉 Tvůj chatbot je připraven k nasazení na skolni-nastenka.cz!**
