# PDF Processing Scripts

Skripty pro zpracování PDF dokumentů pro chatbota.

## Instalace závislostí

```bash
pip install PyPDF2
```

## Použití

### 1. Obecné čtení PDF (pdf_reader.py)

Převede jakýkoliv PDF soubor na textový formát:

```bash
python scripts/pdf_reader.py cesta/k/souboru.pdf
```

Výstup: Vytvoří `.txt` soubor se stejným názvem jako PDF.

**Příklad:**
```bash
python scripts/pdf_reader.py data/documents/organizace_skolniho_roku/Organizace_skolniho_roku\ _2025_26.pdf
```

### 2. Extrakce prázdnin (extract_prazdniny.py)

Automaticky extrahuje informace o prázdninách z PDF dokumentu:

```bash
python scripts/extract_prazdniny.py cesta/k/pdf
```

Pokud nespustíš s parametrem, automaticky použije:
```bash
python scripts/extract_prazdniny.py
```
(Načte výchozí cestu k dokumentu organizace školního roku)

**Výstup:** Vytvoří `prazdniny_2025_26.md` se strukturovanými informacemi o prázdninách.

## Funkce

### pdf_reader.py
- ✅ Čte PDF soubory
- ✅ Extrahuje text po stranách
- ✅ Ukládá do .txt formátu
- ✅ Podpora UTF-8 (čeština)

### extract_prazdniny.py
- ✅ Čte PDF dokumenty
- ✅ Inteligentní vyhledávání prázdnin
- ✅ Kategorizace (podzimní, vánoční, jarní, atd.)
- ✅ Výstup do markdown formátu
- ✅ Automatické formátování

## Extrahované kategorie

- 🍂 Podzimní prázdniny
- 🎄 Vánoční prázdniny
- 📚 Pololetní prázdniny
- 🌸 Jarní prázdniny
- 🐰 Velikonoční prázdniny
- ☀️ Hlavní prázdniny (letní)
- 📅 Další volné dny (státní svátky, ředitelské volno)

## Poznámky

- Skripty vyžadují Python 3.7+
- PyPDF2 se automaticky nainstaluje při prvním spuštění
- Skripty zachovávají český jazyk (UTF-8 encoding)
