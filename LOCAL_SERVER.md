# 🚀 Jak spustit chatbot lokálně

## Problém s `file://` protokolem

Když otevřeš `index.html` přímo v prohlížeči (pomocí `file://`), chatbot nebude fungovat kvůli těmto důvodům:
- **CORS omezení** - prohlížeč blokuje načítání iframe z lokálního souboru
- **Relativní cesty** - JavaScript nemůže správně načíst `config.js` a další soubory

## ✅ Řešení: Lokální HTTP server

### Automatický způsob (doporučený):
```bash
./start_local_server.sh
```

Tento skript automaticky:
1. Spustí Python HTTP server na portu 8080
2. Otevře chatbot v prohlížeči na `http://localhost:8080`

### Manuální způsob:
```bash
cd docs
python3 -m http.server 8080
```

Potom otevři v prohlížeči: http://localhost:8080/index.html

### Pro zastavení serveru:
Stiskni `CTRL+C` v terminálu

## 🌐 Online verze (doporučeno pro testování)

Nejspolehlivější je otestovat přímo na GitHub Pages:
- **Hlavní stránka**: https://tmutina79-png.github.io/chatbot-rag-ready/
- **Samostatný chatbot**: https://tmutina79-png.github.io/chatbot-rag-ready/chat.html

## 📝 Poznámky

- Lokální server je potřeba jen pro **testování před nasazením**
- Pro **produkční použití** použij GitHub Pages verzi
- Backend API běží na Render.com a funguje i s lokálním frontendem
