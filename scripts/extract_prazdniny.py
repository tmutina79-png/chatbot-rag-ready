"""
Extract Prázdniny Script
Skript pro extrakci informací o prázdninách z PDF dokumentu o organizaci školního roku
"""

import sys
import os
import re
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 není nainstalován. Instaluji...")
    os.system("pip install PyPDF2")
    import PyPDF2


def read_pdf(pdf_path):
    """Přečte PDF soubor a vrátí text"""
    text_content = ""
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        for page in pdf_reader.pages:
            text_content += page.extract_text() + "\n"
            
    return text_content


def extract_prazdniny(text):
    """
    Extrahuje informace o prázdninách z textu
    
    Args:
        text: Text z PDF dokumentu
        
    Returns:
        dict: Slovník s informacemi o prázdninách
    """
    prazdniny = {
        'podzimni': [],
        'vanocni': [],
        'pololetni': [],
        'jarni': [],
        'velikonocni': [],
        'hlavni': [],
        'ostatni': []
    }
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Hledáme klíčová slova pro prázdniny
        if 'podzimní' in line_lower and 'prázdniny' in line_lower:
            prazdniny['podzimni'].append(line.strip())
            # Přidáme i následující řádky, které mohou obsahovat data
            if i + 1 < len(lines):
                prazdniny['podzimni'].append(lines[i + 1].strip())
                
        elif 'vánoční' in line_lower and 'prázdniny' in line_lower:
            prazdniny['vanocni'].append(line.strip())
            if i + 1 < len(lines):
                prazdniny['vanocni'].append(lines[i + 1].strip())
                
        elif 'pololetní' in line_lower and 'prázdniny' in line_lower:
            prazdniny['pololetni'].append(line.strip())
            if i + 1 < len(lines):
                prazdniny['pololetni'].append(lines[i + 1].strip())
                
        elif 'jarní' in line_lower and 'prázdniny' in line_lower:
            prazdniny['jarni'].append(line.strip())
            if i + 1 < len(lines):
                prazdniny['jarni'].append(lines[i + 1].strip())
                
        elif 'velikonoční' in line_lower and 'prázdniny' in line_lower:
            prazdniny['velikonocni'].append(line.strip())
            if i + 1 < len(lines):
                prazdniny['velikonocni'].append(lines[i + 1].strip())
                
        elif ('hlavní' in line_lower or 'letní' in line_lower) and 'prázdniny' in line_lower:
            prazdniny['hlavni'].append(line.strip())
            if i + 1 < len(lines):
                prazdniny['hlavni'].append(lines[i + 1].strip())
                
        elif 'volno' in line_lower or 'ředitelské' in line_lower or 'státní svátek' in line_lower:
            prazdniny['ostatni'].append(line.strip())
    
    return prazdniny


def create_markdown(prazdniny, output_path):
    """Vytvoří markdown dokument s prázdninami"""
    
    md_content = "# Prázdniny školního roku 2025/2026\n\n"
    
    if prazdniny['podzimni']:
        md_content += "## 🍂 Podzimní prázdniny\n"
        for item in prazdniny['podzimni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['vanocni']:
        md_content += "## 🎄 Vánoční prázdniny\n"
        for item in prazdniny['vanocni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['pololetni']:
        md_content += "## 📚 Pololetní prázdniny\n"
        for item in prazdniny['pololetni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['jarni']:
        md_content += "## 🌸 Jarní prázdniny\n"
        for item in prazdniny['jarni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['velikonocni']:
        md_content += "## 🐰 Velikonoční prázdniny\n"
        for item in prazdniny['velikonocni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['hlavni']:
        md_content += "## ☀️ Hlavní prázdniny (letní)\n"
        for item in prazdniny['hlavni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    if prazdniny['ostatni']:
        md_content += "## 📅 Další volné dny\n"
        for item in prazdniny['ostatni']:
            if item:
                md_content += f"- {item}\n"
        md_content += "\n"
    
    md_content += "\n---\n\n"
    md_content += "*Automaticky extrahováno z dokumentu Organizace školního roku 2025/2026*\n"
    md_content += f"*Datum vytvoření: 10. prosince 2025*\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return md_content


def main():
    """Hlavní funkce"""
    if len(sys.argv) < 2:
        # Výchozí cesta k PDF
        pdf_path = "/Users/tomasmutina/Documents/Chatbot_skola_1/data/documents/organizace_skolniho_roku/Organizace_skolniho_roku _2025_26.pdf"
    else:
        pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"❌ Soubor nenalezen: {pdf_path}")
        return
    
    print("🔄 Zpracovávám PDF...")
    print(f"📄 Soubor: {os.path.basename(pdf_path)}")
    print("-" * 50)
    
    # Přečteme PDF
    text = read_pdf(pdf_path)
    
    # Extrahujeme prázdniny
    print("🔍 Vyhledávám informace o prázdninách...")
    prazdniny = extract_prazdniny(text)
    
    # Vytvoříme markdown soubor
    output_path = os.path.join(
        os.path.dirname(pdf_path),
        'prazdniny_2025_26.md'
    )
    
    print("📝 Vytvářím markdown dokument...")
    create_markdown(prazdniny, output_path)
    
    print("\n" + "=" * 50)
    print("✅ Hotovo!")
    print(f"📄 Vstupní PDF: {pdf_path}")
    print(f"📝 Výstupní MD: {output_path}")
    print("\n📋 Nalezené prázdniny:")
    
    for typ, items in prazdniny.items():
        if items:
            print(f"\n  {typ.upper()}:")
            for item in items[:2]:  # Zobrazíme max 2 položky z každé kategorie
                if item:
                    print(f"    - {item[:60]}...")


if __name__ == "__main__":
    main()
