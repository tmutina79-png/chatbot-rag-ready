#!/usr/bin/env python3
"""
🧪 Test Script pro ověření API endpointů
Spusť před nasazením: python3 test_api.py
"""

import requests
import sys
from typing import Dict, Any

# Barvy pro terminál
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def test_endpoint(url: str, name: str, method: str = "GET", data: Dict[str, Any] = None) -> bool:
    """Testuje jeden endpoint"""
    try:
        print(f"{BLUE}Testing:{RESET} {name}")
        print(f"  URL: {url}")
        
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print(f"  {GREEN}✓ SUCCESS{RESET} (200 OK)")
            
            # Zobraz část odpovědi
            if isinstance(result, dict):
                if 'success' in result:
                    print(f"  Success: {result['success']}")
                if 'data' in result and isinstance(result['data'], list):
                    print(f"  Data items: {len(result['data'])}")
            
            return True
        else:
            print(f"  {RED}✗ FAILED{RESET} ({response.status_code})")
            print(f"  Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print(f"  {RED}✗ TIMEOUT{RESET} (server neodpovídá)")
        return False
    except requests.exceptions.ConnectionError:
        print(f"  {RED}✗ CONNECTION ERROR{RESET} (server neběží)")
        return False
    except Exception as e:
        print(f"  {RED}✗ ERROR{RESET}: {str(e)}")
        return False
    finally:
        print()

def main():
    """Hlavní testovací funkce"""
    
    # Změň na svou URL
    BASE_URL = input("Zadej API URL (např. http://localhost:8000 nebo https://tvoje-api.onrender.com): ").strip()
    
    if not BASE_URL:
        BASE_URL = "http://localhost:8000"
    
    print(f"\n{YELLOW}{'='*60}{RESET}")
    print(f"{YELLOW}🧪 TESTOVÁNÍ API: {BASE_URL}{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}\n")
    
    results = []
    
    # Test 1: Health check
    results.append(test_endpoint(
        f"{BASE_URL}/",
        "Health Check"
    ))
    
    # Test 2: Vedení školy
    results.append(test_endpoint(
        f"{BASE_URL}/kontakt/vedeni",
        "Kontakt - Vedení školy"
    ))
    
    # Test 3: Učitelé matematiky
    results.append(test_endpoint(
        f"{BASE_URL}/kontakt/ucitele/matematika",
        "Kontakt - Učitelé matematiky"
    ))
    
    # Test 4: Dnešní menu
    results.append(test_endpoint(
        f"{BASE_URL}/jidelna/dnesni-menu",
        "Jídelna - Dnešní menu"
    ))
    
    # Test 5: Týdenní menu
    results.append(test_endpoint(
        f"{BASE_URL}/jidelna/tydenni-menu",
        "Jídelna - Týdenní menu"
    ))
    
    # Test 6: Chat
    results.append(test_endpoint(
        f"{BASE_URL}/chat",
        "Chat - Zpráva",
        method="POST",
        data={"user_id": "test123", "text": "Ahoj"}
    ))
    
    # Výsledky
    print(f"{YELLOW}{'='*60}{RESET}")
    print(f"{YELLOW}📊 VÝSLEDKY:{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}\n")
    
    passed = sum(results)
    total = len(results)
    
    print(f"Úspěšné testy: {GREEN}{passed}/{total}{RESET}")
    print(f"Neúspěšné testy: {RED}{total - passed}/{total}{RESET}\n")
    
    if passed == total:
        print(f"{GREEN}🎉 VŠECHNY TESTY PROŠLY! API je funkční.{RESET}\n")
        print(f"{BLUE}Můžeš pokračovat v nasazení.{RESET}")
        sys.exit(0)
    else:
        print(f"{RED}⚠️  NĚKTERÉ TESTY SELHALY!{RESET}\n")
        print(f"{YELLOW}Doporučení:{RESET}")
        print(f"  1. Zkontroluj, že server běží")
        print(f"  2. Ověř URL endpointů")
        print(f"  3. Zkontroluj logy serveru")
        print(f"  4. Otestuj scraping - stránky se mohly změnit")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Test přerušen uživatelem.{RESET}")
        sys.exit(1)
