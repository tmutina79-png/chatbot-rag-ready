# 🔧 Environment Variables pro Render.com

Pokud používáš citlivé údaje (API klíče, hesla), nastav je jako environment variables na Render.com.

## Jak nastavit na Render.com:

1. Otevři svůj Web Service na Render.com
2. Klikni na **Environment** v levém menu
3. Přidej proměnné pomocí tlačítka **Add Environment Variable**

## Doporučené proměnné:

```env
# Python prostředí
PYTHON_VERSION=3.11

# Port (Render automaticky nastaví)
PORT=10000

# Produkční nastavení
ENVIRONMENT=production

# Příklad: API klíče (pokud používáš)
# OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
```

## V kódu potom používej:

```python
import os

# Získání environment variable
api_key = os.getenv('OPENAI_API_KEY')
environment = os.getenv('ENVIRONMENT', 'development')
port = int(os.getenv('PORT', 8000))

if environment == 'production':
    # Produkční nastavení
    pass
```

## ⚠️ BEZPEČNOST:

- **NIKDY** necommituj soubory `.env` s citlivými údaji
- Používej `.gitignore` pro `.env` soubory
- Environment variables jsou bezpečné - nejsou viditelné v kódu
- Na Render.com jsou zašifrované

---

**Pro tento projekt zatím nejsou žádné citlivé údaje potřeba.**
