#!/bin/bash
# 🚀 QUICK COMMANDS - Chatbot MATIČÁK

echo "════════════════════════════════════════════"
echo "🤖 MATIČÁK - Quick Commands"
echo "════════════════════════════════════════════"
echo ""
echo "Vyber akci:"
echo ""
echo "1) 🧪 Test API (automatický test všech endpointů)"
echo "2) 🚀 Spusť lokálně (backend + frontend)"
echo "3) 🌐 Spusť pro testování ve skupině (lokální síť)"
echo "4) 📦 Připrav k nasazení (kontrola + commit)"
echo "5) 📚 Otevři dokumentaci"
echo "6) ❓ Nápověda"
echo "0) 🚪 Konec"
echo ""
read -p "Tvoje volba (0-6): " choice

case $choice in
    1)
        echo ""
        echo "🧪 Spouštím testy..."
        python3 test_api.py
        ;;
    2)
        echo ""
        echo "🚀 Spouštím lokálně..."
        echo ""
        echo "📌 INSTRUKCE:"
        echo "1. V tomto terminálu se spustí backend"
        echo "2. Otevři NOVÝ terminál a spusť:"
        echo "   cd app/ui && python3 -m http.server 3000"
        echo "3. Otevři prohlížeč: http://localhost:3000/chat.html"
        echo ""
        read -p "Pokračovat? (y/n) " confirm
        if [ "$confirm" = "y" ]; then
            source .venv/bin/activate
            uvicorn main:app --reload --port 8000
        fi
        ;;
    3)
        echo ""
        ./start_local_testing.sh
        ;;
    4)
        echo ""
        echo "📦 Příprava k nasazení..."
        echo ""
        
        # Kontrola config.js
        echo "1️⃣ Kontroluji config.js..."
        if grep -q "127.0.0.1:8000" app/ui/config.js; then
            echo "   ⚠️  WARNING: config.js stále používá localhost!"
            echo "   Změň URL v app/ui/config.js na produkční backend"
            read -p "   Chceš pokračovat? (y/n) " cont
            if [ "$cont" != "y" ]; then
                exit 0
            fi
        else
            echo "   ✅ config.js je nastaven na produkční URL"
        fi
        
        # Test
        echo ""
        echo "2️⃣ Chceš spustit testy? (y/n)"
        read -p "   " test
        if [ "$test" = "y" ]; then
            python3 test_api.py
            if [ $? -ne 0 ]; then
                echo "   ❌ Testy selhaly!"
                exit 1
            fi
        fi
        
        # Git
        echo ""
        echo "3️⃣ Git commit a push"
        echo "   Současný status:"
        git status -s
        echo ""
        read -p "   Commit message: " msg
        if [ -z "$msg" ]; then
            msg="Ready for deployment"
        fi
        git add .
        git commit -m "$msg"
        git push origin main
        
        echo ""
        echo "✅ Hotovo!"
        echo ""
        echo "📋 Další kroky:"
        echo "1. Počkej 2-3 minuty na GitHub Actions build"
        echo "2. Zkontroluj: https://github.com/TVOJE_JMENO/chatbot-rag-ready/actions"
        echo "3. Otevři GitHub Pages URL"
        echo "4. Otestuj všechny funkce"
        echo ""
        ;;
    5)
        echo ""
        echo "📚 Dokumentace:"
        echo ""
        echo "📖 README.md - Přehled projektu"
        echo "🚀 DEPLOYMENT.md - Návod na nasazení"
        echo "✅ DEPLOYMENT_CHECKLIST.md - Checklist"
        echo "🧪 TESTING.md - Testování"
        echo "👥 TESTING_INSTRUCTIONS_FOR_USERS.md - Pro účastníky"
        echo "🔗 USEFUL_LINKS.md - Užitečné odkazy"
        echo "📝 CHANGES_SUMMARY.md - Souhrn změn"
        echo ""
        read -p "Který soubor otevřít? (např. DEPLOYMENT.md): " doc
        if [ -f "$doc" ]; then
            if command -v code &> /dev/null; then
                code "$doc"
            else
                cat "$doc"
            fi
        fi
        ;;
    6)
        echo ""
        echo "❓ NÁPOVĚDA"
        echo ""
        echo "🔧 Základní příkazy:"
        echo ""
        echo "  # Aktivace virtuálního prostředí"
        echo "  source .venv/bin/activate"
        echo ""
        echo "  # Spuštění backendu"
        echo "  uvicorn main:app --reload --port 8000"
        echo ""
        echo "  # Spuštění frontendu"
        echo "  cd app/ui && python3 -m http.server 3000"
        echo ""
        echo "  # Test API"
        echo "  python3 test_api.py"
        echo ""
        echo "  # Git"
        echo "  git status"
        echo "  git add ."
        echo "  git commit -m 'message'"
        echo "  git push origin main"
        echo ""
        echo "📚 Více informací:"
        echo "  - README.md - Základy"
        echo "  - DEPLOYMENT.md - Nasazení"
        echo "  - TESTING.md - Testování"
        echo ""
        ;;
    0)
        echo ""
        echo "👋 Nashledanou!"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Neplatná volba"
        exit 1
        ;;
esac
