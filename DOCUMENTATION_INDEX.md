# 📚 Dokumentace - Index

Vítej v dokumentaci chatbota MATIČÁK! Tento soubor ti pomůže zorientovat se ve všech návodech.

---

## 🚀 Pro rychlý start

### ⚡ **[QUICKSTART.md](QUICKSTART.md)** - ZAČNI TADY!
**Co najdeš:** Nasazení za 10 minut, krok za krokem
**Kdy použít:** Chceš rychle nasadit a nezajímají tě detaily
**Čas:** 10-15 minut

### 📖 **[README.md](README.md)** - Přehled projektu
**Co najdeš:** Základní info, quick start, struktura projektu
**Kdy použít:** První seznámení s projektem

---

## 🌐 Pro nasazení

### 🚀 **[DEPLOYMENT.md](DEPLOYMENT.md)** - Kompletní návod
**Co najdeš:** 
- Detailní návod na nasazení backendu (Render, Railway, PythonAnywhere)
- Konfigurace frontendu
- CORS nastavení
- Řešení problémů
- Alternativa: lokální síť

**Kdy použít:** Chceš pochopit celý proces nasazení

### ✅ **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Checklist
**Co najdeš:** 
- Checklist pro každý krok nasazení
- Místo pro poznámky
- Zaznamenání problémů a řešení

**Kdy použít:** Během nasazování, abys nic nezapomněl

---

## 🧪 Pro testování

### 🔬 **[TESTING.md](TESTING.md)** - Testování před nasazením
**Co najdeš:**
- Automatický test script
- Manuální testovací postup
- Test scrapingu
- Kontrola v konzoli

**Kdy použít:** Před nasazením do produkce

### 👥 **[TESTING_INSTRUCTIONS_FOR_USERS.md](TESTING_INSTRUCTIONS_FOR_USERS.md)**
**Co najdeš:**
- Návod pro účastníky testování
- Co testovat
- Jak nahlásit problémy
- FAQ

**Kdy použít:** Pošli účastníkům společně s URL

---

## 🔧 Technická dokumentace

### ⚙️ **[ENVIRONMENT_VARIABLES.md](ENVIRONMENT_VARIABLES.md)**
**Co najdeš:**
- Návod na env variables
- Bezpečnostní tipy
- Příklady použití

**Kdy použít:** Když používáš API klíče nebo citlivé údaje

### 🔗 **[USEFUL_LINKS.md](USEFUL_LINKS.md)**
**Co najdeš:**
- Odkazy na hosting platformy
- Dokumentace technologií
- Učební materiály
- Komunity a podpora

**Kdy použít:** Hledáš další zdroje nebo pomoc

---

## 📝 Informační dokumenty

### 📋 **[CHANGES_SUMMARY.md](CHANGES_SUMMARY.md)**
**Co najdeš:**
- Souhrn všech změn pro nasazení
- Statistiky
- Co je potřeba změnit před nasazením

**Kdy použít:** Chceš přehled, co všechno bylo uděláno

---

## 🛠️ Skripty a nástroje

### 🧪 **[test_api.py](test_api.py)** - Automatický test
**Co dělá:** Testuje všechny API endpointy
**Jak použít:**
```bash
python3 test_api.py
```

### 🌐 **[start_local_testing.sh](start_local_testing.sh)** - Lokální testování
**Co dělá:** Spustí server pro testování ve skupině (lokální síť)
**Jak použít:**
```bash
./start_local_testing.sh
```

### ⚡ **[quick_commands.sh](quick_commands.sh)** - Rychlé příkazy
**Co dělá:** Interaktivní menu s užitečnými příkazy
**Jak použít:**
```bash
./quick_commands.sh
```

---

## 📊 Doporučený postup

### Pro první nasazení:

```
1. Přečti README.md (5 min)
2. Následuj QUICKSTART.md (10-15 min)
3. Otestuj podle TESTING.md (5 min)
4. Sdílej s účastníky + TESTING_INSTRUCTIONS_FOR_USERS.md
```

### Pro důkladné pochopení:

```
1. README.md → základy
2. DEPLOYMENT.md → detailní návod
3. DEPLOYMENT_CHECKLIST.md → používej během procesu
4. TESTING.md → před i po nasazení
5. USEFUL_LINKS.md → další studium
```

### Pro problémy:

```
1. DEPLOYMENT.md → sekce "Řešení problémů"
2. TESTING.md → kontrola API
3. USEFUL_LINKS.md → Stack Overflow, komunity
```

---

## 🎯 Které dokumenty pro kterou situaci?

### "Chci rychle nasadit"
→ **QUICKSTART.md**

### "Chci pochopit, jak to funguje"
→ **README.md** + **DEPLOYMENT.md**

### "Něco nefunguje"
→ **TESTING.md** + **DEPLOYMENT.md** (Řešení problémů)

### "Nasazuji poprvé"
→ **QUICKSTART.md** + **DEPLOYMENT_CHECKLIST.md**

### "Potřebuji testovat"
→ **TESTING.md** + `test_api.py`

### "Sdílím s účastníky"
→ **TESTING_INSTRUCTIONS_FOR_USERS.md**

### "Hledám další zdroje"
→ **USEFUL_LINKS.md**

### "Chci vědět, co bylo změněno"
→ **CHANGES_SUMMARY.md**

---

## 📞 Kontakt a podpora

Máš problém s dokumentací nebo něco nefunguje?

1. Zkontroluj **DEPLOYMENT.md** → sekci "Řešení problémů"
2. Zkontroluj **USEFUL_LINKS.md** → Stack Overflow odkazy
3. Otevři issue na GitHubu
4. Kontaktuj autory projektu

---

## 🔄 Aktualizace dokumentace

Dokumentace je průběžně aktualizována. 

**Poslední update:** 8. prosince 2025

**Našel jsi chybu?** Klidně otevři pull request nebo issue!

---

## ✅ Quick Reference

```bash
# Základní příkazy

# Test API
python3 test_api.py

# Lokální testování
./start_local_testing.sh

# Quick commands menu
./quick_commands.sh

# Spustit backend
source .venv/bin/activate
uvicorn main:app --reload --port 8000

# Spustit frontend
cd app/ui && python3 -m http.server 3000

# Git workflow
git add .
git commit -m "message"
git push origin main
```

---

**Happy coding! 🚀**

**Vytvořeno pro Matiční gymnázium Ostrava** ❤️
