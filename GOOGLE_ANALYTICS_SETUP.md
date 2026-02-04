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

### Krok 1: Vytvoření Google Analytics účtu (DETAILNÍ NÁVOD)

#### 1.1 Registrace
1. **Otevřete prohlížeč** a přejděte na: https://analytics.google.com/
2. **Přihlaste se** Google účtem školy (nebo vytvořte nový)
3. Klikněte na tlačítko **"Začít měřit"** (Start measuring)

#### 1.2 Nastavení účtu
1. **Název účtu:** Zadejte např. `Matiční gymnázium Ostrava`
2. **Sdílení dat účtu:** Ponechte výchozí nastavení (doporučené benchmarky)
3. Klikněte **"Další"**

#### 1.3 Vytvoření vlastnosti (Property)
1. **Název vlastnosti:** `MATIČÁK Chatbot` nebo `MGO Chatbot`
2. **Časové pásmo:** Vyberte `(GMT+01:00) Prague`
3. **Měna:** Vyberte `Czech Koruna (CZK)` nebo `Euro (EUR)`
4. Klikněte **"Další"**

#### 1.4 Informace o firmě
1. **Odvětví:** Vyberte `Education` (Vzdělávání)
2. **Velikost firmy:** Vyberte podle počtu zaměstnanců školy
3. Klikněte **"Další"**

#### 1.5 Cíle měření
Zaškrtněte:
- ✅ **"Examine user behavior"** (Analyzovat chování uživatelů)
- ✅ **"Measure customer engagement"** (Měřit zapojení)
3. Klikněte **"Vytvořit"**

#### 1.6 Přijetí podmínek
1. Přečtěte si podmínky služby
2. ✅ Zaškrtněte souhlas
3. Klikněte **"Přijmout"**

#### 1.7 Vytvoření datového streamu (DATA STREAM)
1. GA vám nabídne "Nastavte sběr dat"
2. Klikněte na **"Web"** (ikonka 🌐)
3. **URL webu:** `https://tmutina79-png.github.io`
4. **Název streamu:** `MATIČÁK Chatbot - GitHub Pages`
5. Klikněte **"Vytvořit stream"**

#### 1.8 🎉 Hotovo! Zkopírujte Measurement ID
Na nové obrazovce uvidíte:
```
Podrobnosti datového streamu

Measurement ID: G-ABC123DEF4
              ↑↑↑↑↑↑↑↑↑↑↑↑
         TOHLE ZKOPÍRUJTE!
```

**💡 TIP:** Measurement ID najdete vždy v:
- **Správce** (Admin) → **Datové streamy** → Klikněte na stream → **Measurement ID** nahoře

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
- **Přesný text každé zprávy** (v event_label)
- Čas, kdy uživatelé píší nejčastěji

**💡 Nejdůležitější:** V Google Analytics uvidíte:
- Co lidé nejčastěji vyhledávají (jména učitelů, třídy, předměty...)
- Které dotazy se opakují
- Na co chatbot neumí odpovědět

### Událost: click
Sledování kliknutí na tlačítka podle kategorie:
- **Button/Kontakt** - kolikrát uživatelé hledají kontakty
- **Button/Jídelna** - zájem o jídelníček
- **Button/Rozvrh** - kontrola rozvrhu
- **Button/Ostatní** - další informace
- **Button/Novinky** - zájem o aktuality

### Jak zobrazit data v GA4

#### 📊 Zobrazení všech zpráv uživatelů

1. V Google Analytics přejděte na **Správy** → **Události**
2. Najděte událost **`chat_message`**
3. Klikněte na ni
4. Uvidíte seznam všech odeslaných zpráv v kolonce **"event_label"**

**💡 Co uvidíte:**
```
event_label                    | Počet
-------------------------------------------
"rozvrh PA"                    | 45×
"jaká je dnes jídelna"         | 32×
"kontakt na paní učitelku XY"  | 28×
"kdy máme matematiku"          | 19×
"suplování"                    | 15×
```

#### 📈 Vytvoření vlastního reportu

1. Přejděte na **Průzkumník** (Explore) v levém menu
2. Klikněte **"+ Nový průzkum"**
3. Vyberte **"Prázdný průzkum"**
4. Nastavte:
   - **Dimenze:** Přidejte `Štítek události` (Event label)
   - **Metriky:** Přidejte `Počet událostí`
5. Přetáhněte dimenze a metriky do tabulky
6. Filtrujte pouze událost `chat_message`

Výsledek: **Přehledná tabulka všech dotazů seřazených podle četnosti!**

#### 🕐 Nejaktivnější časy

1. V **Průzkumníku** vytvořte nový report
2. **Dimenze:** `Hodina` + `Den v týdnu`
3. **Metriky:** `Počet událostí`
4. **Filtr:** `Název události = chat_message`

Uvidíte: **Kdy studenti používají chatbot nejčastěji** (např. před 1. hodinou, o přestávkách...)

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
