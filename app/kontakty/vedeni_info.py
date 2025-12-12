"""
Informace o vedení a správě školy
Zdroj: https://mgo.cz/jj/kontakty/vedeni-a-sprava-skoly.html
Aktualizováno: 12.12.2025
"""

VEDENI_SKOLY = [
    {
        "jmeno": "Mgr. Vasevič Ladislav",
        "pozice": "Ředitel školy",
        "email": "",
        "telefon": "+420 596 11 88 77, linka 103"
    },
    {
        "jmeno": "PaedDr. Mohelník Karel",
        "pozice": "Zástupce ředitele",
        "email": "",
        "telefon": "+420 596 11 62 38, linka 104"
    },
    {
        "jmeno": "Mgr. Čeledová Platošová Zdeňka",
        "pozice": "Zástupce ředitele",
        "email": "",
        "telefon": "+420 596 11 62 38, linka 102"
    }
]


def get_vedeni_info_text():
    """Vrátí formátovaný text s informacemi o vedení školy"""
    text = "👔 Vedení školy - Matiční gymnázium Ostrava\n\n"
    
    for osoba in VEDENI_SKOLY:
        text += f"▪️ {osoba['jmeno']}\n"
        text += f"   Pozice: {osoba['pozice']}\n"
        text += f"   📧 Email: {osoba['email']}\n"
        text += f"   📞 Telefon: {osoba['telefon']}\n\n"
    
    return text


def get_vedeni_info_dict():
    """Vrátí informace o vedení jako slovník"""
    return VEDENI_SKOLY
