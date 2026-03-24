# 🤖 MATIČÁK Chatbot – Integrace do Joomla 3

## Přehled

Existují **3 způsoby** nasazení chatbota do Joomla 3 (od nejjednoduššího):

| Způsob | Obtížnost | Přístup |
|--------|-----------|---------|
| A) Custom HTML modul | ⭐ Nejsnazší | Přes administraci |
| B) Úprava šablony | ⭐⭐ Střední | Editace souboru šablony |
| C) Vlastní plugin | ⭐⭐⭐ Pokročilý | Vytvoření Joomla pluginu |

---

## Varianta A) Custom HTML modul (doporučeno) ⭐

Nejrychlejší způsob – vše uděláte přes administraci Joomla.

### Krok 1: Nahrát soubor widgetu na server

1. Připojte se na server přes **FTP** (FileZilla, WinSCP apod.)
2. Vytvořte složku: `/media/maticak/`
3. Nahrajte soubor `chatbot-widget-v2.js` do `/media/maticak/`

> Soubor najdete v: `web-integration/chatbot-widget-v2.js` nebo `docs/chatbot-widget-v2.js`

### Krok 2: Vytvořit Custom HTML modul

1. Přihlaste se do **Administrace Joomla** → `Rozšíření` → `Moduly`
2. Klikněte na **Nový** → vyberte typ **Vlastní HTML** (Custom HTML)
3. Nastavte:
   - **Název:** `MATIČÁK Chatbot`
   - **Pozice:** Vyberte pozici, která je na VŠECH stránkách (např. `debug` nebo `footer`)
   - **Stav:** Publikováno
   - **Přiřazení menu:** Na všech stránkách
4. V editoru přepněte na **režim zdrojového kódu** (tlačítko `<>` nebo `Toggle editor`)
5. Vložte tento kód:

```html
<script src="/media/maticak/chatbot-widget-v2.js"></script>
<script>
  MaticakChatbot.init({
    chatbotUrl: 'https://tmutina79-png.github.io/chatbot-rag-ready/chat.html'
  });
</script>
```

6. Klikněte na **Uložit & zavřít**

### ⚠️ Důležité: Vypnout filtrování HTML

Joomla 3 ve výchozím nastavení odstraňuje `<script>` tagy z Custom HTML modulů.

**Řešení:**

1. Jděte do `Rozšíření` → `Moduly` → otevřete modul `MATIČÁK Chatbot`
2. Přejděte na záložku **Možnosti** (Options)
3. Nastavte **Připravit obsah** (Prepare Content): `Ne`
4. Jděte do `Systém` → `Globální nastavení` → `Filtry textu`
5. Pro skupinu **Super Users** nastavte filtr na: `Bez filtrování` (No Filtering)
6. Uložte

---

## Varianta B) Úprava šablony ⭐⭐

Spolehlivější metoda – přímo editujete soubor šablony.

### Krok 1: Nahrát widget na server

Stejné jako v Variantě A – nahrajte `chatbot-widget-v2.js` do `/media/maticak/`.

### Krok 2: Editace šablony

1. Přihlaste se do **Administrace Joomla**
2. Jděte do `Rozšíření` → `Šablony` → `Šablony` (záložka)
3. Klikněte na svou **aktivní šablonu** (např. `protostar`, `Gantry` atd.)
4. Otevřete soubor `index.php` šablony
5. **Před uzavírací tag `</body>`** vložte:

```php
<!-- MATIČÁK Chatbot Widget -->
<script src="<?php echo JURI::root(); ?>media/maticak/chatbot-widget-v2.js"></script>
<script>
  MaticakChatbot.init({
    chatbotUrl: 'https://tmutina79-png.github.io/chatbot-rag-ready/chat.html'
  });
</script>
```

6. Uložte soubor

### Alternativa: Přes Template Override

Pokud nechcete měnit přímo `index.php`, vytvořte **template override**:

1. Vytvořte soubor `/templates/VASE_SABLONA/html/mod_custom/default.php`
2. Tím se zabrání přepsání při aktualizaci šablony

---

## Varianta C) Vlastní Joomla plugin ⭐⭐⭐

Nejčistší řešení – chatbot se automaticky vloží na všechny stránky.

### Krok 1: Vytvořit strukturu pluginu

Na serveru vytvořte tyto soubory:

**Soubor: `/plugins/system/maticakchatbot/maticakchatbot.xml`**

```xml
<?xml version="1.0" encoding="utf-8"?>
<extension version="3.0" type="plugin" group="system" method="upgrade">
    <name>MATIČÁK Chatbot</name>
    <author>Matiční gymnázium Ostrava</author>
    <version>1.0.0</version>
    <description>Vloží MATIČÁK chatbot widget na všechny stránky webu.</description>
    <files>
        <filename plugin="maticakchatbot">maticakchatbot.php</filename>
        <folder>media</folder>
    </files>
    <config>
        <fields name="params">
            <fieldset name="basic">
                <field
                    name="chatbot_url"
                    type="url"
                    default="https://tmutina79-png.github.io/chatbot-rag-ready/chat.html"
                    label="URL chatbotu"
                    description="URL adresa chatbot rozhraní (chat.html)"
                />
                <field
                    name="enabled_frontend"
                    type="radio"
                    default="1"
                    label="Zobrazit na frontendu"
                    description="Povolit chatbot na veřejné části webu"
                >
                    <option value="0">Ne</option>
                    <option value="1">Ano</option>
                </field>
            </fieldset>
        </fields>
    </config>
</extension>
```

**Soubor: `/plugins/system/maticakchatbot/maticakchatbot.php`**

```php
<?php
defined('_JEXEC') or die;

class PlgSystemMaticakchatbot extends JPlugin
{
    /**
     * Vloží chatbot widget před uzavírací </body> tag
     */
    public function onBeforeCompileHead()
    {
        $app = JFactory::getApplication();

        // Pouze na frontendu (ne v administraci)
        if ($app->isAdmin()) {
            return;
        }

        // Zkontrolovat, zda je povoleno
        if (!$this->params->get('enabled_frontend', 1)) {
            return;
        }
    }

    public function onAfterRender()
    {
        $app = JFactory::getApplication();

        // Pouze na frontendu
        if ($app->isAdmin()) {
            return;
        }

        if (!$this->params->get('enabled_frontend', 1)) {
            return;
        }

        $chatbotUrl = $this->params->get(
            'chatbot_url',
            'https://tmutina79-png.github.io/chatbot-rag-ready/chat.html'
        );

        // Widget script
        $widgetScript = '
<script src="' . JUri::root() . 'media/plg_system_maticakchatbot/chatbot-widget-v2.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    MaticakChatbot.init({
      chatbotUrl: "' . htmlspecialchars($chatbotUrl, ENT_QUOTES, 'UTF-8') . '"
    });
  });
</script>';

        // Vložit před </body>
        $body = $app->getBody();
        $body = str_replace('</body>', $widgetScript . "\n</body>", $body);
        $app->setBody($body);
    }
}
```

### Krok 2: Nahrát soubory widgetu

Nahrajte `chatbot-widget-v2.js` do:
```
/media/plg_system_maticakchatbot/chatbot-widget-v2.js
```

### Krok 3: Aktivovat plugin

1. Jděte do `Rozšíření` → `Správce pluginů`
2. Vyhledejte **MATIČÁK Chatbot**
3. **Povolte** plugin (klikněte na červený křížek → změní se na zelená fajfka)
4. Otevřete plugin a nastavte URL chatbotu dle potřeby

### Alternativa: Instalace přes ZIP

1. Zabalte složku `maticakchatbot/` do ZIP souboru
2. V administraci: `Rozšíření` → `Správce rozšíření` → `Nahrát soubor balíčku`
3. Nahrajte ZIP soubor

---

## 🔧 Použití s vlastním backendem (widget v1)

Pokud máte **vlastní backend server** a chcete použít plný widget (v1 – přímá komunikace s API):

```html
<script src="/media/maticak/chatbot-widget.js"></script>
<script>
  MaticakChatbot.init({
    apiUrl: 'https://deploy-web-service-enfc.onrender.com'
  });
</script>
```

Nahrajte `chatbot-widget.js` (z `web-integration/`) místo v2 verze.

---

## ❓ Řešení problémů

### Chatbot se nezobrazuje

1. **Zkontrolujte konzoli prohlížeče** (F12 → Console) – hledejte chyby
2. **Ověřte cestu k souboru** – navštivte `https://vase-domena.cz/media/maticak/chatbot-widget-v2.js` – měl by se zobrazit JavaScript kód
3. **Joomla filtruje `<script>` tagy** – viz sekce o vypnutí filtrování v Variantě A
4. **Cache** – vymažte Joomla cache: `Systém` → `Vymazat mezipaměť`

### Widget překrývá obsah

Upravte z-index v inicializaci:
```javascript
MaticakChatbot.init({
  chatbotUrl: 'https://tmutina79-png.github.io/chatbot-rag-ready/chat.html'
});
```
Případně přidejte vlastní CSS do šablony:
```css
#maticak-chatbot-iframe { z-index: 99999 !important; }
#maticak-chat-toggle { z-index: 99998 !important; }
```

### Chatbot nereaguje / API chyby

- Ověřte, že backend běží: navštivte `https://deploy-web-service-enfc.onrender.com/health`
- Zkontrolujte CORS nastavení backendu – musí povolit doménu vašeho Joomla webu

---

## 📋 Shrnutí

| Co nahrát | Kam | Kdy |
|-----------|-----|-----|
| `chatbot-widget-v2.js` | `/media/maticak/` | Varianta A, B |
| `chatbot-widget-v2.js` | `/media/plg_system_maticakchatbot/` | Varianta C |
| `chatbot-widget.js` | `/media/maticak/` | Pokud používáte vlastní backend |

**Doporučení:** Pro rychlé nasazení použijte **Variantu A** (Custom HTML modul). Pro produkční web použijte **Variantu C** (plugin).
