import sys
import time
import argparse
import requests
import socket
import shutil
import subprocess
from urllib.parse import urlparse
from pathlib import Path

def try_get(url, timeout):
    try:
        r = requests.get(url, timeout=timeout)
        return r.status_code, r.headers, r.text[:1000], None
    except Exception as e:
        return None, None, None, e

def is_port_open(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True, None
    except Exception as e:
        return False, e

def find_uvicorn_process():
    try:
        # portable fallback: ps aux and search for 'uvicorn'
        out = subprocess.check_output(["ps", "aux"], text=True)
        lines = [l for l in out.splitlines() if "uvicorn" in l and "grep" not in l]
        return lines
    except Exception:
        return []

def check_uvicorn_installed():
    return shutil.which("uvicorn") is not None

def check_ui_files():
    # opravena cesta do kořene projektu (parents[1] místo parents[2])
    base = Path(__file__).resolve().parents[1] / "app" / "ui"
    files = {
        "chat.html": (base / "chat.html").exists(),
        "config.js": (base / "config.js").exists(),
        "chatbot.js": (base / "chatbot.js").exists()
    }
    return base, files

def find_listening_processes(port):
    """
    Zkusí najít procesy, které poslouchají na daném portu pomocí lsof / ss / netstat.
    Vrací seznam (cmd, line) nebo prázdný list.
    """
    cmds = [
        ["lsof", "-iTCP:%d" % port, "-sTCP:LISTEN", "-P", "-n"],
        ["ss", "-ltnp"],
        ["netstat", "-ltnp"]
    ]
    results = []
    for cmd in cmds:
        try:
            out = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL)
            for l in out.splitlines():
                # jednoduchý filtr podle portu v řádku
                if f":{port}" in l or f" {port} " in l or f".{port}" in l:
                    results.append((" ".join(cmd), l.strip()))
        except Exception:
            # příkaz nemusí být dostupný na systému, ignorujeme
            continue
    return results

def check_backend(base_url, timeout=2.0, retries=3, verbose=False, check_ui=False):
    parsed = urlparse(base_url if "://" in base_url else "http://" + base_url)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    if verbose:
        print(f"Kontroluji host {host} port {port} (scheme={parsed.scheme})")

    port_ok, port_err = is_port_open(host, port, timeout=1.0)
    if port_ok:
        print(f"✅ TCP port {port} na {host} je otevřený")
    else:
        print(f"❌ TCP port {port} na {host} je uzavřen nebo nelze dosáhnout. Chyba: {port_err}")
        # doplňující diagnostika: zkusíme zjistit, zda nějaký proces poslouchá na portu
        listeners = find_listening_processes(port)
        if listeners:
            print("⚠️ Naslouchající procesy nalezeny (výpis z lsof/ss/netstat):")
            for cmd, line in listeners:
                print(f" - [{cmd}] {line}")
            print("Možné příčiny: proces poslouchá na jiném rozhraní (např. 0.0.0.0 nebo specifické IP),")
            print("nebo firewall/iptables blokuje spojení z tohoto rozhraní.")
        else:
            print("ℹ️ Nebyly nalezeny žádné procesy, které by poslouchaly na tom portu.")
        print("Doporučení: spusť backend (aktivuj venv) -> uvicorn main:app --reload --port 8000 --host 127.0.0.1")
        print("Pokud chceš dostupnost i z jiné sítě, použij --host 0.0.0.0 a případně nastav firewall.")
        # budeme pokračovat s HTTP kontrolami pro dodatečné informace

    # rozšířená HTTP kontrola: zkusíme i 'localhost' vs '127.0.0.1'
    endpoints = ["", "/openapi.json", "/docs"]
    endpoints_ok = True

    targets = [base_url.rstrip("/")]
    # pokud base_url používá 127.0.0.1, přidej alternativu localhost, a naopak
    if "127.0.0.1" in base_url:
        targets.append(base_url.replace("127.0.0.1", "localhost").rstrip("/"))
    elif "localhost" in base_url:
        targets.append(base_url.replace("localhost", "127.0.0.1").rstrip("/"))
    else:
        # přidej explicitně obě lokální varianty pro test
        targets.extend([f"http://127.0.0.1:{port}", f"http://localhost:{port}"])

    for target_base in dict.fromkeys(targets):  # deduplikuje
        if verbose:
            print(f"Testuji cílovou základní URL: {target_base}")
        for ep in endpoints:
            url = target_base + ep
            success = False
            last_err = None
            for attempt in range(1, retries + 1):
                if verbose:
                    print(f"Pokouším se {url} (pokus {attempt}/{retries})...")
                code, headers, body_snippet, err = try_get(url, timeout)
                if code is not None:
                    if 200 <= code < 400:
                        print(f"✅ {url} odpověděl kódem {code}")
                    else:
                        print(f"⚠️ {url} odpověděl kódem {code}")
                    if verbose and headers:
                        try:
                            print(f"  headers: {dict(headers)}")
                        except Exception:
                            print(f"  headers: {headers}")
                        print(f"  body ukázka: {body_snippet!r}")
                    success = True
                    break
                else:
                    last_err = err
                    if verbose:
                        print(f"  chyba: {err}")
                time.sleep(0.3)
            if not success:
                endpoints_ok = False
                print(f"❌ Nelze načíst {url}. Poslední chyba: {last_err}")

    # uvicorn/process checks
    uv_installed = check_uvicorn_installed()
    procs = find_uvicorn_process()
    if uv_installed:
        print("✅ 'uvicorn' je dostupný v PATH")
    else:
        print("⚠️ 'uvicorn' není v PATH. Ujisti se, že jsi aktivoval virtuální prostředí.")
    if procs:
        print("✅ Nalezené běžící procesy s 'uvicorn':")
        for l in procs:
            print("  " + l.strip())
    else:
        print("⚠️ Nebyl nalezen běžící proces obsahující 'uvicorn' (ps aux search).")

    if check_ui:
        base_path, files = check_ui_files()
        print(f"Kontrola UI souborů v {base_path}:")
        for name, exists in files.items():
            print(f" - {name}: {'✅' if exists else '❌'}")
        if not all(files.values()):
            print("Doporučení: zkopíruj nebo obnov soubory do app/ui/ (chat.html, config.js, chatbot.js)")

    # výsledek považujeme za OK pokud alespoň HTTP endpointy odpovídají (port upozorníme zvlášť)
    all_ok = endpoints_ok
    return all_ok

def main():
    parser = argparse.ArgumentParser(description="Kontrola dostupnosti FastAPI backendu.")
    parser.add_argument("--url", "-u", default="http://127.0.0.1:8000", help="Základní URL backendu")
    parser.add_argument("--timeout", "-t", type=float, default=2.0, help="Timeout v sekundách pro jednotlivé požadavky")
    parser.add_argument("--retries", "-r", type=int, default=3, help="Počet opakovaných pokusů pro každý endpoint")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose výstup")
    parser.add_argument("--check-ui", action="store_true", help="Zkontrolovat existenci základních UI souborů")
    args = parser.parse_args()

    ok = check_backend(args.url, timeout=args.timeout, retries=args.retries, verbose=args.verbose, check_ui=args.check_ui)
    if not ok:
        print("\nDoporučení:")
        print(" - Aktivuj virtuální prostředí: source .venv/bin/activate")
        print(" - Spusť backend: uvicorn main:app --reload --port 8000")
        print(" - Pokud používáš jiný port, přepni --url (např. --url http://127.0.0.1:8080)")
        sys.exit(2)
    else:
        print("\nVše v pořádku.")
        sys.exit(0)

if __name__ == "__main__":
    main()
