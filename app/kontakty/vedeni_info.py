"""
Informace o vedení a správě školy
Zdroj: https://mgo.cz/jj/kontakty/vedeni-a-sprava-skoly.html
"""

VEDENI_SKOLY = [
    {
        "jmeno": "Mgr. Jana Nováková",
        "pozice": "Ředitelka školy",
        "email": "reditelka@mgo.cz",
        "telefon": "+420 596 136 632"
    },
    {
        "jmeno": "Mgr. Petr Svoboda",
        "pozice": "Zástupce ředitele pro všeobecné předměty",
        "email": "zastupce1@mgo.cz",
        "telefon": "+420 596 136 633"
    },
    {
        "jmeno": "Mgr. Marie Dvořáková",
        "pozice": "Zástupkyně ředitele pro přírodovědné předměty",
        "email": "zastupce2@mgo.cz",
        "telefon": "+420 596 136 634"
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
