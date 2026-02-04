# 📊 Google Analytics - Návod k nastavení

## ✅ Co už je implementováno

Chatbot je připravený na sledování těchto událostí:

### 1. **Odesílání zpráv do chatu**
- Event: `chat_message`
- Kategorie: `Chat`
- Sleduje: délku zprávy, počet odeslaných zpráv

### 2. **Klikání na tlačítka**
- Event: `click`
- Kategorie: `Button`
- Sleduje kliknutí na:
  - 📧 Kontakt
  - 🍽️ Jídelna
  - 📅 Rozvrh
  - 📋 Ostatní
  - 🔔 Novinky (NOVÉ)

## 🚀 Jak aktivovat Google Analytics

### Krok 1: Vytvoření Google Analytics účtu

1. Přejděte na https://analytics.google.com/
2. Přihlaste se Google účtem
3. Klikněte na **"Začít měřit"**
4. Vytvořte **Účet** (např. "Matiční gymnázium")
5. Vytvořte **Vlastnost** (Property) - např. "MATIČÁK Chatbot"
6. Vyberte **"Web"** jako platformu
7. Zadejte URL: `https://tmutina79-png.github.io`
8. Klikněte na **"Vytvořit datový stream"**

### Krok 2: Získání Measurement ID

Po vytvoření datového streamu získáte **Measurement ID** ve formátu:
```
G-XXXXXXXXXX
```

Tento ID najdete v nastavení vlastnosti → Datové streamy → Web stream

### Krok 3: Nahrazení placeholder ID v kódu

V souborech:
- `docs/chat.html` (řádky 8 a 13)
- `app/ui/chat.html` (řádky 8 a 13)

Nahraďte `G-XXXXXXXXXX` svým skutečným Measurement ID:

```html
<!-- Před: -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    gtag('config', 'G-XXXXXXXXXX');
</script>

<!-- Po: -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ABC123DEF4"></script>
<script>
    gtag('config', 'G-ABC123DEF4');
</script>
```

### Krok 4: Nasazení změn

```bash
git add docs/chat.html app/ui/chat.html
git commit -m "feat: Přidáno skutečné Google Analytics Measurement ID"
git push origin main
```

### Krok 5: Ověření funkčnosti

1. Otevřete chatbot na https://tmutina79-png.github.io/chatbot-rag-ready/chat.html
2. Otevřete konzoli prohlížeče (F12 → Console)
3. Klikněte na některé tlačítko nebo odešlete zprávu
4. V konzoli uvidíte: `GA Event: Button - click - Jídelna`
5. Po 24-48 hodinách se data zobrazí v Google Analytics dashboardu

## 📈 Co uvidíte v Google Analytics

### Událost: chat_message
- Počet odeslaných zpráv
- Průměrná délka zpráv
- Čas, kdy uživatelé píší nejčastěji

### Událost: click
Sledování kliknutí na tlačítka podle kategorie:
- **Button/Kontakt** - kolikrát uživatelé hledají kontakty
- **Button/Jídelna** - zájem o jídelníček
- **Button/Rozvrh** - kontrola rozvrhu
- **Button/Ostatní** - další informace
- **Button/Novinky** - zájem o aktuality

### Jak zobrazit data v GA4

1. Přihlaste se do Google Analytics
2. Vlevo → **Události** (Events)
3. Uvidíte tabulku všech sledovaných událostí
4. Klikněte na událost pro detail
5. Vytvořte vlastní reporty v sekci **Průzkumník** (Explore)

## 🔍 Tipy pro analýzu

### Nejpoužívanější funkce
V sekci **Události** seřaďte podle počtu událostí:
- Které tlačítko je nejoblíbenější?
- Píšou uživatelé zprávy nebo používají tlačítka?

### Časová analýza
V **Průzkumníku** vytvořte graf:
- Kdy je chatbot nejvíce používán? (ráno, odpoledne, večer)
- Který den v týdnu je nejaktivnější?

### Chování uživatelů
Sledujte:
- Průměrný čas na stránce
- Míra okamžitého opuštění (bounce rate)
- Počet interakcí na návštěvu

## 🛠️ Pokročilé možnosti

### Přidání vlastních dimenzí
Můžete rozšířit tracking o:
- Typ dotazu (rozvrh konkrétní třídy, učitel, menu...)
- Úspěšnost odpovědí (našel/nenašel informaci)
- Typ zařízení (mobil/desktop)

### Propojení s Search Console
Pro sledování, jak uživatelé nacházejí chatbot přes Google vyhledávání.

## 📞 Podpora

Pokud narazíte na problém:
1. Zkontrolujte, že Measurement ID je správně zkopírované
2. Ověřte v konzoli prohlížeče, že se logy vypisují
3. Počkejte 24-48 hodin na zobrazení dat v GA4
4. Zkontrolujte, že stránka běží přes HTTPS (ne file://)

---

**Vytvořeno:** 4. února 2026  
**Status:** ✅ Implementace dokončena, čeká na aktivaci Measurement ID
