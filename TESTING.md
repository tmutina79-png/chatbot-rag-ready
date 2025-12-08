# 🧪 Testování před nasazením

Před nasazením do produkce **VŽDY** otestuj vše lokálně!

## Rychlý test

```bash
# 1. Spusť backend
source .venv/bin/activate
uvicorn main:app --reload --port 8000

# 2. V druhém terminálu spusť automatický test
python3 test_api.py
```

Zadej: `http://localhost:8000`

## Ruční testování v prohlížeči

### 1. Otevři API dokumentaci
```
http://localhost:8000/docs
```

### 2. Otevři frontend
```
# Spusť HTTP server
cd app/ui
python3 -m http.server 3000

# Otevři v prohlížeči
http://localhost:3000/chat.html
```

### 3. Otestuj funkce

#### ✅ Chatbot se zobrazí
- [x] Widget v pravém dolním rohu
- [x] Uvítací zpráva s typing efektem
- [x] Tlačítka "Kontakt" a "Jídelna"

#### ✅ Kontakt
- [x] Klikni na tlačítko "Kontakt"
- [x] Modal se otevře
- [x] Klikni "Vedení školy"
  - Zobrazí se jména, pozice, emaily, telefony
  - Emaily jsou klikací (mailto:)
- [x] Klikni "Učitelé"
  - Zobrazí se předměty
  - Klikni na "Matematika"
  - Zobrazí se učitelé matematiky
  - Emaily jsou klikací

#### ✅ Jídelna
- [x] Klikni na tlačítko "Jídelna"
- [x] Modal se otevře
- [x] Postupně se načte dnešní menu
  - Oběd 1
  - Oběd 2
  - BL (pokud je k dispozici)
- [x] Klikni "Týdenní menu"
- [x] Modal se zavře
- [x] V chatu se postupně zobrazí týdenní menu
  - Každý den zvlášť
  - Všechny tři typy jídel
  - Správné formátování (nadpisy, odstavce)

#### ✅ Chat funkce
- [x] Napiš zprávu do inputu
- [x] Klikni "Odeslat"
- [x] Zpráva se zobrazí vpravo (modrá bublina)
- [x] Typing indicator se objeví
- [x] Bot odpoví (bílá bublina)
- [x] Typing efekt při odpovědi

#### ✅ Typing efekt
- [x] Klikni tlačítko "⚡ Přeskočit typing"
- [x] Text se zobrazí okamžitě

#### ✅ Responsivita
- [x] Zmáčkni F12 (DevTools)
- [x] Přepni na mobilní view
- [x] Widget se správně zobrazuje
- [x] Všechny funkce fungují

## Konzole prohlížeče (F12)

Zkontroluj záložku **Console**:
- ❌ Žádné červené chyby
- ❌ Žádné varování ohledně CORS
- ✅ Pouze info logi

Zkontroluj záložku **Network**:
- ✅ Všechny požadavky (vedeni, ucitele, jidelna) mají status 200
- ✅ Response obsahuje data (ne prázdné pole)

## Test API přímo

```bash
# Vedení
curl http://localhost:8000/kontakt/vedeni | python3 -m json.tool

# Učitelé
curl http://localhost:8000/kontakt/ucitele/matematika | python3 -m json.tool

# Dnešní menu
curl http://localhost:8000/jidelna/dnesni-menu | python3 -m json.tool

# Týdenní menu
curl http://localhost:8000/jidelna/tydenni-menu | python3 -m json.tool

# Chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"test","text":"Ahoj"}' | python3 -m json.tool
```

Každý endpoint by měl vrátit:
```json
{
  "success": true,
  "data": [...]
}
```

## Testování scrapingu

Scraping může selhat, pokud se změnila struktura stránek:

### Kontakty
```python
python3 -c "from app.kontakty.scraper import scrape_vedeni_skoly; print(scrape_vedeni_skoly())"
```

Mělo by vrátit seznam slovníků s vedením.

### Jídelna
```python
python3 -c "from app.jidelna.scraper import scrape_dnesni_menu; print(scrape_dnesni_menu())"
```

Mělo by vrátit dnešní menu s 3 typy jídel.

## Co dělat když něco nefunguje

### Backend se nespustí
```bash
# Reinstaluj závislosti
pip install -r requirements.txt --force-reinstall

# Zkontroluj Python verzi
python3 --version  # Mělo by být 3.8+
```

### Scraping nefunguje
- Stránka může být nedostupná
- HTML struktura se mohla změnit
- Zkontroluj internet připojení
- Otevři cílovou stránku v prohlížeči

### Frontend nenačítá data
- Zkontroluj `config.js` - správná URL?
- Backend běží?
- Konzole prohlížeče - nějaké chyby?

## ✅ Checklist před nasazením

- [ ] ✅ Všechny automatické testy prošly (`python3 test_api.py`)
- [ ] ✅ Manuálně otestovány všechny funkce
- [ ] ✅ Žádné chyby v konzoli prohlížeče
- [ ] ✅ Scraping funguje (data se načítají)
- [ ] ✅ Chat odpovídá
- [ ] ✅ Typing efekt funguje
- [ ] ✅ Tlačítka jsou funkční

**Pokud vše funguje → můžeš nasadit do produkce! 🚀**

Návod: [DEPLOYMENT.md](DEPLOYMENT.md)
