#!/bin/bash

# 🎨 Barvy pro output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# 🎯 ASCII Art Banner
clear
echo -e "${BLUE}"
cat << "EOF"
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║     🤖 CHATBOT DEPLOY HELPER - Render.com 🚀         ║
║                                                       ║
║     Automatický průvodce nasazením                   ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# ✅ Kontrola stavu
echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Kontroluji stav projektu...${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

# Zkontroluj Git status
if [ -d ".git" ]; then
    echo -e "${GREEN}✓${NC} Git repository nalezen"
else
    echo -e "${RED}✗${NC} Toto není Git repository!"
    exit 1
fi

# Zkontroluj důležité soubory
files_to_check=("main.py" "requirements.txt" "render.yaml" "data/skolni_data.json" "app/core/data_manager.py")
for file in "${files_to_check[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} $file CHYBÍ!"
        exit 1
    fi
done

# Zkontroluj vzdálený repozitář
remote_url=$(git remote get-url origin 2>/dev/null)
if [ -n "$remote_url" ]; then
    echo -e "${GREEN}✓${NC} GitHub remote: $remote_url"
else
    echo -e "${RED}✗${NC} GitHub remote není nastaven!"
    exit 1
fi

# Zkontroluj nevyzáložkované změny
if [ -n "$(git status --porcelain)" ]; then
    echo -e "\n${YELLOW}⚠${NC}  Máš nevyzáložkované změny:"
    git status --short
    echo -e "\n${YELLOW}Chceš je commitnout a pushnout? (y/n)${NC}"
    read -r answer
    if [ "$answer" = "y" ]; then
        echo -e "${BLUE}📝 Zadej commit message:${NC}"
        read -r commit_msg
        git add -A
        git commit -m "$commit_msg"
        git push origin main
        echo -e "${GREEN}✓${NC} Změny pushnuty na GitHub"
    fi
else
    echo -e "${GREEN}✓${NC} Všechny změny jsou na GitHubu"
fi

# 🚀 Návod na Render.com
echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🚀 KROK 1: Registrace a Nasazení na Render.com${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "1. Otevři prohlížeč a jdi na: ${GREEN}https://render.com${NC}"
echo -e "2. Klikni na ${BLUE}\"Get Started for Free\"${NC}"
echo -e "3. Vyber ${BLUE}\"Sign Up with GitHub\"${NC}"
echo -e "4. Autorizuj Render.com"
echo -e "5. Klikni na ${BLUE}\"New +\"${NC} → ${BLUE}\"Web Service\"${NC}"
echo -e "6. Najdi repository: ${GREEN}chatbot-rag-ready${NC}"
echo -e "7. Nastav:"
echo -e "   ${YELLOW}•${NC} Name: ${GREEN}chatbot-backend${NC}"
echo -e "   ${YELLOW}•${NC} Region: ${GREEN}Frankfurt (EU Central)${NC}"
echo -e "   ${YELLOW}•${NC} Branch: ${GREEN}main${NC}"
echo -e "   ${YELLOW}•${NC} Build Command: ${GREEN}pip install -r requirements.txt${NC}"
echo -e "   ${YELLOW}•${NC} Start Command: ${GREEN}uvicorn main:app --host 0.0.0.0 --port \$PORT${NC}"
echo -e "   ${YELLOW}•${NC} Instance Type: ${GREEN}Free${NC}"
echo -e "8. Klikni na ${BLUE}\"Create Web Service\"${NC}"

echo -e "\n${YELLOW}⏳ Build bude trvat 5-10 minut...${NC}"
echo -e "${YELLOW}💡 Během buildování můžeš sledovat logy v reálném čase.${NC}"

echo -e "\n${BLUE}Stiskni ENTER až bude build hotový a dostaneš URL...${NC}"
read -r

# 🌐 Získání URL
echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}🌐 KROK 2: Test Backend API${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "${BLUE}Zadej URL tvého Render.com backendu:${NC}"
echo -e "${YELLOW}(např. https://chatbot-backend-xyz.onrender.com)${NC}"
read -r backend_url

# Odstranění trailing slash
backend_url="${backend_url%/}"

echo -e "\n${GREEN}🧪 Testuji backend na $backend_url...${NC}\n"

# Test vedení školy
echo -e "${BLUE}📋 Test 1: Vedení školy${NC}"
response=$(curl -s -w "\n%{http_code}" "$backend_url/kontakt/vedeni")
http_code=$(echo "$response" | tail -n 1)
body=$(echo "$response" | head -n -1)

if [ "$http_code" = "200" ]; then
    echo -e "${GREEN}✓${NC} HTTP 200 OK"
    if echo "$body" | grep -q '"success":true'; then
        echo -e "${GREEN}✓${NC} Data načtena úspěšně"
        source=$(echo "$body" | grep -o '"source":"[^"]*"' | cut -d'"' -f4)
        echo -e "${GREEN}✓${NC} Zdroj dat: $source"
    else
        echo -e "${RED}✗${NC} Chyba v odpovědi"
    fi
else
    echo -e "${RED}✗${NC} HTTP $http_code - Něco se nepovedlo!"
fi

# Test menu
echo -e "\n${BLUE}🍽️  Test 2: Dnešní menu${NC}"
response=$(curl -s -w "\n%{http_code}" "$backend_url/jidelna/dnesni-menu")
http_code=$(echo "$response" | tail -n 1)

if [ "$http_code" = "200" ]; then
    echo -e "${GREEN}✓${NC} HTTP 200 OK"
else
    echo -e "${RED}✗${NC} HTTP $http_code - Něco se nepovedlo!"
fi

# Test rozvrhu
echo -e "\n${BLUE}📅 Test 3: Rozvrh KVA${NC}"
response=$(curl -s -w "\n%{http_code}" "$backend_url/rozvrh/kva")
http_code=$(echo "$response" | tail -n 1)

if [ "$http_code" = "200" ]; then
    echo -e "${GREEN}✓${NC} HTTP 200 OK"
else
    echo -e "${RED}✗${NC} HTTP $http_code - Něco se nepovedlo!"
fi

# 📝 Aktualizace config.js
echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📝 KROK 3: Aktualizace GitHub Pages Config${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "${YELLOW}Aktualizuji docs/config.js s tvou Render.com URL...${NC}"

# Backup původního config.js
cp docs/config.js docs/config.js.backup

# Aktualizace URL v config.js
sed -i.bak "s|const API_URL = \"http://127.0.0.1:8000\";|const API_URL = \"$backend_url\";|g" docs/config.js
sed -i.bak "s|const API_URL = \"https://[^\"]*\";|const API_URL = \"$backend_url\";|g" docs/config.js
rm docs/config.js.bak

echo -e "${GREEN}✓${NC} config.js aktualizován"

# Commit a push
echo -e "\n${YELLOW}Commituju a pushuju změny...${NC}"
git add docs/config.js
git commit -m "Aktualizace API URL na Render.com backend: $backend_url"
git push origin main

echo -e "${GREEN}✓${NC} Změny pushnuty na GitHub"
echo -e "${YELLOW}⏳ GitHub Pages se aktualizují (1-2 minuty)...${NC}"

# 🎉 Finální info
echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 HOTOVO! Chatbot je online!${NC}"
echo -e "${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

github_username=$(git remote get-url origin | sed -n 's/.*github.com[:/]\([^/]*\)\/.*/\1/p')
repo_name=$(git remote get-url origin | sed -n 's/.*\/\(.*\)\.git/\1/p')

echo -e "${BLUE}🌐 Odkazy:${NC}"
echo -e "   ${YELLOW}•${NC} Chatbot: ${GREEN}https://$github_username.github.io/$repo_name/${NC}"
echo -e "   ${YELLOW}•${NC} Backend API: ${GREEN}$backend_url${NC}"
echo -e "   ${YELLOW}•${NC} GitHub Repo: ${GREEN}https://github.com/$github_username/$repo_name${NC}"
echo -e "   ${YELLOW}•${NC} Render Dashboard: ${GREEN}https://dashboard.render.com${NC}"

echo -e "\n${BLUE}📋 Co dál:${NC}"
echo -e "   ${YELLOW}1.${NC} Otevři chatbot URL v prohlížeči"
echo -e "   ${YELLOW}2.${NC} Vyzkoušej všechny funkce"
echo -e "   ${YELLOW}3.${NC} Sdílej s ostatními!"

echo -e "\n${YELLOW}💡 Tipy:${NC}"
echo -e "   ${YELLOW}•${NC} První načtení po dlouhé době může trvat 30-60 sekund (cold start)"
echo -e "   ${YELLOW}•${NC} Render.com Free tier vypíná server po 15 minutách nečinnosti"
echo -e "   ${YELLOW}•${NC} Pro aktualizaci dat uprav ${GREEN}data/skolni_data.json${NC} a pushni změny"
echo -e "   ${YELLOW}•${NC} Render.com automaticky znovu nasadí při každém pushu na GitHub"

echo -e "\n${GREEN}✨ Děkuji za použití! Užij si svůj chatbot! ✨${NC}\n"

# Nabídka otevření v prohlížeči
echo -e "${BLUE}Chceš otevřít chatbot v prohlížeči? (y/n)${NC}"
read -r answer
if [ "$answer" = "y" ]; then
    chatbot_url="https://$github_username.github.io/$repo_name/"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open "$chatbot_url"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open "$chatbot_url"
    else
        echo -e "${YELLOW}Otevři v prohlížeči: $chatbot_url${NC}"
    fi
fi

echo -e "\n${PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
