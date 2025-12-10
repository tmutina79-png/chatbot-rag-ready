"""
PDF Reader Script
Skript pro čtení a konverzi PDF souborů do textového formátu
"""

import sys
import os
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("PyPDF2 není nainstalován. Instaluji...")
    os.system("pip install PyPDF2")
    import PyPDF2


def read_pdf(pdf_path):
    """
    Přečte PDF soubor a vrátí jeho textový obsah
    
    Args:
        pdf_path: Cesta k PDF souboru
        
    Returns:
        str: Textový obsah PDF
    """
    try:
        text_content = ""
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"📄 Načítám PDF: {os.path.basename(pdf_path)}")
            print(f"📊 Počet stran: {num_pages}")
            print("-" * 50)
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                text_content += f"\n--- Strana {page_num + 1} ---\n"
                text_content += text
                
        return text_content
        
    except Exception as e:
        return f"❌ Chyba při čtení PDF: {str(e)}"


def save_to_txt(text_content, pdf_path):
    """
    Uloží textový obsah do .txt souboru
    
    Args:
        text_content: Text k uložení
        pdf_path: Původní cesta k PDF (pro vytvoření názvu txt souboru)
    """
    # Vytvoříme název pro txt soubor
    txt_path = pdf_path.replace('.pdf', '.txt')
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text_content)
    
    print(f"✅ Text uložen do: {txt_path}")
    return txt_path


def main():
    """Hlavní funkce"""
    if len(sys.argv) < 2:
        print("❌ Použití: python pdf_reader.py <cesta_k_pdf>")
        print("Příklad: python pdf_reader.py document.pdf")
        return
    
    pdf_path = sys.argv[1]
    
    if not os.path.exists(pdf_path):
        print(f"❌ Soubor nenalezen: {pdf_path}")
        return
    
    if not pdf_path.lower().endswith('.pdf'):
        print("❌ Soubor není PDF")
        return
    
    # Přečteme PDF
    print("🔄 Zpracovávám PDF...")
    text_content = read_pdf(pdf_path)
    
    # Uložíme do txt
    txt_path = save_to_txt(text_content, pdf_path)
    
    print("\n" + "=" * 50)
    print("✅ Hotovo!")
    print(f"📄 PDF: {pdf_path}")
    print(f"📝 TXT: {txt_path}")


if __name__ == "__main__":
    main()
