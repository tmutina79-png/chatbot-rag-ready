#!/bin/bash

# 🚀 Skript pro spuštění chatbota pro lokální testování se skupinou

echo "🤖 MATIČÁK - Spouštění pro testování..."
echo ""

# Zjistit IP adresu
echo "📡 Zjišťuji IP adresu..."
IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1)

if [ -z "$IP" ]; then
    echo "❌ Nepodařilo se zjistit IP adresu"
    echo "   Zjisti ji ručně pomocí: ifconfig"
    exit 1
fi

echo "✅ Tvoje IP adresa: $IP"
echo ""

# Kontrola virtuálního prostředí
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtuální prostředí neexistuje. Vytvářím..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

echo "📦 Virtuální prostředí aktivováno"
echo ""

# Spustit backend
echo "🔧 Spouštím backend server..."
echo "   Backend URL: http://$IP:8001"
echo ""

# Zobrazit URL pro účastníky
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📱 URL PRO ÚČASTNÍKY:"
echo ""
echo "   http://$IP:8001"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⚠️  DŮLEŽITÉ:"
echo "   1. Všichni musí být ve stejné WiFi síti"
echo "   2. V app/ui/config.js nastav: API_BASE_URL: 'http://$IP:8001'"
echo "   3. V druhém terminálu spusť:"
echo "      cd app/ui && python3 -m http.server 3000"
echo "   4. Účastníci otevřou: http://$IP:3000/chat.html"
echo ""
echo "📚 API dokumentace: http://$IP:8001/docs"
echo ""
echo "🛑 Pro zastavení stiskni Ctrl+C"
echo ""

# Spustit server
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
