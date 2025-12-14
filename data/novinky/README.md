# Novinky Chatbota MATIČÁK

Tato složka obsahuje aktuální novinky a oznámení zobrazované v chatbotu.

## Struktura

### novinky.json
Hlavní soubor obsahující všechny novinky ve formátu JSON.

## Formát novinky

```json
{
  "id": 1,
  "datum": "YYYY-MM-DD",
  "nadpis": "Nadpis novinky",
  "ikona": "📋",
  "kategorie": "Důležité|Akce|Technologie|Info",
  "obsah": {
    // Flexibilní struktura podle typu novinky
  },
  "aktivni": true|false
}
```

## Kategorie novinek

- **Důležité** - Přijímací řízení, termíny, důležitá oznámení
- **Akce** - Školní akce, prázdniny, akce
- **Technologie** - Nové funkce, aktualizace systémů
- **Info** - Obecné informace

## Správa novinek

1. **Přidat novou novinku:** Přidej nový objekt do pole `novinky` v `novinky.json`
2. **Deaktivovat novinku:** Nastav `"aktivni": false`
3. **Ikony:** Použij emoji pro vizuální reprezentaci (📋 🎄 🤖 📅 🎉 ⚠️ 📢)

## Priorita zobrazení

Novinky jsou zobrazeny:
1. Od nejnovějšího data
2. Pouze aktivní (`"aktivni": true`)
3. Maximum 5 posledních novinek

## Příklad použití

Chatbot automaticky načte novinky z tohoto souboru a zobrazí je v modálním okně "NOVÉ".
