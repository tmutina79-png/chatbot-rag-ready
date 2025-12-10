#!/bin/bash

# 🚀 Quick Deploy Script pro GitHub Pages
# Tento skript rychle nasadí změny na GitHub Pages

echo "🚀 MATIČÁK - GitHub Pages Deployment"
echo "====================================="
echo ""

# Zkontroluj, že jsme ve správném adresáři
if [ ! -f "main.py" ]; then
    echo "❌ Chyba: Spusť tento skript v root složce projektu!"
    exit 1
fi

echo "📋 Kroky:"
echo "1. Zkopírovat nejnovější verzi chat.html"
echo "2. Commitnout změny"
echo "3. Pushnout na GitHub"
echo ""

# Zkopíruj nejnovější verzi
echo "📁 Kopíruji chat.html do docs/..."
cp app/ui/chat.html docs/chat.html

# Zkopíruj config.js
if [ -f "app/ui/config.js" ]; then
    echo "📁 Kopíruji config.js do docs/..."
    cp app/ui/config.js docs/config.js
fi

# Git status
echo ""
echo "📊 Git status:"
git status docs/

# Zeptej se, jestli pokračovat
echo ""
read -p "✅ Pokračovat s commitem a pushem? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Commit
    echo "💾 Commitování..."
    git add docs/
    git commit -m "Update chatbot on GitHub Pages"
    
    # Push
    echo "📤 Nahrávání na GitHub..."
    git push origin main
    
    echo ""
    echo "✅ HOTOVO!"
    echo ""
    echo "🌐 Tvůj chatbot bude za 1-2 minuty dostupný na:"
    echo "   https://tmutina79-png.github.io/chatbot-rag-ready/"
    echo ""
else
    echo "❌ Zrušeno."
fi
