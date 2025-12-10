#!/bin/bash

# 🚀 Quick Deploy Script pro Render.com backend

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🚀 RENDER.COM BACKEND DEPLOYMENT                         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Zkontroluj, že jsme ve správném adresáři
if [ ! -f "main.py" ]; then
    echo "❌ Chyba: Spusť tento skript v root složce projektu!"
    exit 1
fi

echo "📋 Tento skript ti pomůže nasadit backend na Render.com"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎯 CO BUDEŠ POTŘEBOVAT:"
echo "  1. GitHub účet"
echo "  2. 10 minut času"
echo "  3. Tento repozitář pushnutý na GitHub"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 KROKY:"
echo ""
echo "1️⃣  Jdi na: https://render.com"
echo "2️⃣  Zaregistruj se pomocí GitHub"
echo "3️⃣  Klikni 'New +' → 'Web Service'"
echo "4️⃣  Připoj tento repozitář: chatbot-rag-ready"
echo ""
read -p "⏸️  Zmáčkni ENTER až toto uděláš..."
echo ""
echo "5️⃣  Nastav konfiguraci:"
echo ""
echo "    Name:           maticak-backend"
echo "    Region:         Frankfurt (EU Central)"
echo "    Branch:         main"
echo "    Runtime:        Python 3"
echo "    Build Command:  pip install -r requirements.txt"
echo "    Start Command:  uvicorn main:app --host 0.0.0.0 --port \$PORT"
echo "    Instance Type:  Free"
echo ""
read -p "⏸️  Zmáčkni ENTER až toto vyplníš..."
echo ""
echo "6️⃣  Klikni 'Create Web Service' a počkej 5-10 minut"
echo ""
read -p "⏸️  Zmáčkni ENTER až je backend nasazený..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Backend by měl být teď online!"
echo ""
echo "🔗 Zkopíruj URL z Render.com (např. https://maticak-backend.onrender.com)"
echo ""
read -p "Zadej URL backendu: " BACKEND_URL

if [ -z "$BACKEND_URL" ]; then
    echo "❌ URL je prázdná!"
    exit 1
fi

echo ""
echo "📝 Aktualizuji config.js s novou URL..."
echo ""

# Aktualizuj docs/config.js
cat > docs/config.js << EOF
// Konfigurace API endpointů
const CONFIG = {
    // Produkční backend na Render.com
    API_BASE_URL: '${BACKEND_URL}'
};
EOF

echo "✅ Soubor docs/config.js aktualizován!"
echo ""
echo "📤 Nahrávám změny na GitHub..."
echo ""

# Commit a push
git add docs/config.js render.yaml RENDER_DEPLOYMENT.md
git commit -m "🚀 Configure backend for Render.com deployment

Backend URL: ${BACKEND_URL}
"
git push origin main

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🎉 HOTOVO!"
echo ""
echo "🌐 Tvůj chatbot je teď plně funkční na:"
echo ""
echo "  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"
echo "  ┃  https://tmutina79-png.github.io/chatbot-rag-ready/  ┃"
echo "  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"
echo ""
echo "📱 Otevři URL a vyzkoušej všechny funkce!"
echo ""
echo "🧪 TESTUJ:"
echo "  ✅ Kontakt → Vedení školy"
echo "  ✅ Jídelna → Dnešní menu"
echo "  ✅ Rozvrh → Třída KVA"
echo "  ✅ AI chat"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 DALŠÍ KROKY:"
echo "  📊 Sleduj logy na Render.com dashboardu"
echo "  🔗 Sdílej URL s ostatními"
echo "  🎨 Přizpůsob design (barvy, text, logo)"
echo ""
echo "📚 Dokumentace: RENDER_DEPLOYMENT.md"
echo ""
