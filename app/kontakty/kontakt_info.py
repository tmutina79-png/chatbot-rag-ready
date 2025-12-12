"""
Konfigurace kontaktních informací pro chatbota
Zdroj: https://mgo.cz/jj/kontakty.html
Aktualizováno: 12.12.2025
"""

KONTAKT_INFO = {
    "nazev": "Matiční gymnázium Ostrava",
    "adresa": "Mánesova 1/7, 702 00 Ostrava-Moravská Ostrava",
    "email": "skopkova@mgo.cz",  # Sekretariát školy
    "telefon": "+420 596 116 239",
    "web": "https://www.mgo.cz",
    "uredni_hodiny": {
        "pondeli": "7:00 - 15:00",
        "utery": "7:00 - 15:00",
        "streda": "7:00 - 15:00",
        "ctvrtek": "7:00 - 15:00",
        "patek": "7:00 - 15:00"
    },
    "social_media": {
        "facebook": "https://www.facebook.com/MaticniGO",
        "instagram": "@maticnigymnazivm"
    },
    "popis": "Matiční gymnázium je moderní škola s dlouhou tradicí, zaměřená na komplexní rozvoj studentů v akademické i lidské oblasti."
}


def get_kontakt_text():
    """Vrátí formátovaný kontaktní text pro zobrazení"""
    return f"""📧 Kontakt

{KONTAKT_INFO['nazev']}

📍 Adresa: {KONTAKT_INFO['adresa']}
📧 E-mail: {KONTAKT_INFO['email']}
📞 Telefon: {KONTAKT_INFO['telefon']}
🌐 Web: {KONTAKT_INFO['web']}

Úřední hodiny:
Po-Čt: 8:00 - 16:00
Pá: 8:00 - 14:00

Sledujte nás:
Facebook: {KONTAKT_INFO['social_media']['facebook']}
Instagram: {KONTAKT_INFO['social_media']['instagram']}
"""


def get_kontakt_html():
    """Vrátí HTML formátovaný kontaktní text"""
    return f"""
    <div style="font-family: 'Segoe UI', sans-serif; padding: 20px;">
        <h2 style="color: #667eea; margin-bottom: 15px;">📧 Kontakt</h2>
        <h3 style="color: #333; margin-bottom: 10px;">{KONTAKT_INFO['nazev']}</h3>
        
        <p style="margin: 8px 0;"><strong>📍 Adresa:</strong><br>{KONTAKT_INFO['adresa']}</p>
        <p style="margin: 8px 0;"><strong>📧 E-mail:</strong> <a href="mailto:{KONTAKT_INFO['email']}">{KONTAKT_INFO['email']}</a></p>
        <p style="margin: 8px 0;"><strong>📞 Telefon:</strong> <a href="tel:{KONTAKT_INFO['telefon']}">{KONTAKT_INFO['telefon']}</a></p>
        <p style="margin: 8px 0;"><strong>🌐 Web:</strong> <a href="{KONTAKT_INFO['web']}" target="_blank">{KONTAKT_INFO['web']}</a></p>
        
        <h4 style="color: #667eea; margin-top: 15px; margin-bottom: 5px;">Úřední hodiny:</h4>
        <p style="margin: 4px 0;">Pondělí - Čtvrtek: 8:00 - 16:00</p>
        <p style="margin: 4px 0;">Pátek: 8:00 - 14:00</p>
        
        <h4 style="color: #667eea; margin-top: 15px; margin-bottom: 5px;">Sledujte nás:</h4>
        <p style="margin: 4px 0;">Facebook: <a href="{KONTAKT_INFO['social_media']['facebook']}" target="_blank">MaticniGO</a></p>
        <p style="margin: 4px 0;">Instagram: {KONTAKT_INFO['social_media']['instagram']}</p>
    </div>
    """


def get_kontakt_json():
    """Vrátí kontaktní informace jako JSON"""
    return KONTAKT_INFO
