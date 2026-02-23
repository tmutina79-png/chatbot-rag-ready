#!/bin/bash

# Skript pro spuštění lokálního serveru a otevření chatbota v prohlížeči

echo "🚀 Spouštím lokální server..."
echo ""
echo "📂 Adresář: docs/"
echo "🌐 URL: http://localhost:8080"
echo ""
echo "⚠️  Pro zastavení serveru stiskni CTRL+C"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd "$(dirname "$0")/docs"

# Otevřít prohlížeč
sleep 1
open http://localhost:8080/index.html

# Spustit server
python3 -m http.server 8080
