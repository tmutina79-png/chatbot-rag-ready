"""
Pravidlová logika pro odpovědi MATIČČÁKA
"""
import random

class RuleBasedResponder:
    def __init__(self):
        self.greetings = ["ahoj", "čau", "dobrý den", "dobré odpoledne", "nazdar", "zdravím", "čus", "zdar"]
        self.identity_keywords = ["kdo jsi", "co jsi", "kdo seš", "představ se", "kdo ses", "co ses"]
        self.help_keywords = ["pomoc", "pomoct", "pomůžeš", "nevím", "nerozumím", "poraď", "poradíš"]
        self.thanks_keywords = ["děkuji", "díky", "děkuju", "dekuji", "dík", "diky", "dekuju"]
        self.school_keywords = ["škola", "skola", "vyučování", "vyucovani", "třída", "trida", "studium"]
        self.schedule_keywords = ["rozvrh", "hodina", "kdy mám", "kdy je", "kdy začíná", "kdy zacina"]
        self.subjects_keywords = ["předmět", "predmet", "matematika", "čeština", "cestina", "angličtina", "anglictina", "fyzika", "chemie", "dějepis", "dejepis"]
        self.motivation_keywords = ["unavený", "unaveny", "těžké", "tezke", "nezvládám", "nezvladam", "nemůžu", "nemuzu"]
        self.goodbye_keywords = ["nashle", "nashledanou", "čau", "cau", "ahoj", "zatim", "zatím"]
        
    def get_response(self, user_message: str) -> str:
        """
        Vrací odpověď založenou na klíčových slovech v uživatelské zprávě
        """
        message_lower = user_message.lower()
        
        # Pozdravy
        if any(greeting in message_lower for greeting in self.greetings):
            if any(keyword in message_lower for keyword in self.identity_keywords):
                return self._identity_response()
            return random.choice([
                "Ahoj! Jsem MATIČÁK, tvůj školní AI pomocník. 👋 Jak ti můžu pomoci?",
                "Nazdar! 😊 Jsem MATIČÁK a jsem tu pro tebe! Co potřebuješ?",
                "Čau! 👋 MATIČÁK tady. Jak se vede? S čím můžu pomoct?"
            ])
        
        # Identita
        if any(keyword in message_lower for keyword in self.identity_keywords):
            return self._identity_response()
        
        # Poděkování
        if any(keyword in message_lower for keyword in self.thanks_keywords):
            return random.choice([
                "Rád jsem pomohl! 😊 Pokud budeš něco potřebovat, jsem tu pro tebe.",
                "Není zač! 🎉 Kdykoliv budeš potřebovat, klidně se ozvi!",
                "Ale jo! 💪 To je přece moje práce - pomáhat ti!"
            ])
        
        # Motivace
        if any(keyword in message_lower for keyword in self.motivation_keywords):
            return self._motivation_response()
        
        # Pomoc
        if any(keyword in message_lower for keyword in self.help_keywords):
            return self._help_response()
        
        # Rozvrh
        if any(keyword in message_lower for keyword in self.schedule_keywords):
            return "Bohužel zatím nemám přístup k rozvrhu. 📅 Ale pracuju na tom! Brzy to bude lepší."
        
        # Předměty
        if any(keyword in message_lower for keyword in self.subjects_keywords):
            return "Rád bych ti pomohl s předměty! 📚 V budoucnu budu umět vysvětlovat matematiku, češtinu, angličtinu a další předměty. Zatím se učím!"
        
        # Škola obecně
        if any(keyword in message_lower for keyword in self.school_keywords):
            return "Jsem tu, abych ti pomohl se vším, co souvisí se školou! 🎓 Ptej se na cokoliv."
        
        # Defaultní odpověď
        return self._default_response()
    
    def _identity_response(self) -> str:
        return """Jsem MATIČÁK - Matiční AI Pomocník! 🤖

Jsem tu, abych ti pomohl se školou:
• Odpovídám na dotazy
• Vysvětluji učivo
• Pomáhám s plánováním
• A mnoho dalšího!

Na čem můžu pomoct?"""
    
    def _help_response(self) -> str:
        return """Samozřejmě ti pomůžu! 💪

Můžeš se mě zeptat na:
• Informace o škole
• Vysvětlení učiva
• Rady ke studiu
• Organizaci času

Co tě zajímá?"""
    
    def _motivation_response(self) -> str:
        return random.choice([
            """Chápu, že to může být náročné! 💪 Ale věř mi, zvládneš to!

Zkus:
• Udělat si pauzu a projít se
• Rozdělit úkol na menší kousky
• Pochválit se za každý malý pokrok

Jsem tady, pokud budeš potřebovat pomoc! 🌟""",
            """Hele, neboj! Všichni někdy máme horší dny. 😊

Pamatuj:
• Krok po kroku se dojde daleko
• Chyby jsou součást učení
• Jsi lepší, než si myslíš!

Co kdybychom to zkusili společně? 🚀""",
            """To je v pohodě, stává se! 🤗

Tip ode mě:
• Dej si kratší přestávku
• Vrať se k tomu s čistou hlavou
• Zeptej se, když něčemu nerozumíš

Společně to dáme! 💙"""
        ])
    
    def _default_response(self) -> str:
        return random.choice([
            """Hmm, úplně nerozumím, co tím myslíš. 🤔

Zkus zadat konkrétní klíčové slovo:
• Rozvrh, Jídelna, Kontakty
• Předmět (matematika, fyzika...)
• Učitel + předmět
• Klikni nahoře na tlačítka rychlé volby

Jsem tu pro tebe!""",
            """Nerozpoznávám tento pokyn. 😅

Ale zkus:
• Zadat heslovitý dotaz
• Zeptat se na konkrétní věc
• Uvést klíčové slovo (rozvrh, učitel, menu...)
• Klikni nahoře na tlačítka rychlé volby

Rád ti pomůžu! 🎯""",
            """Ups, nevím, co tím máš na mysli! 😊

Můžeš zkusit:
• Napsat klíčové slovo?
• Uvést konkrétní dotaz?
• Kliknout nahoře na tlačítka rychlé volby

Jsem tady pro tebe! 💫"""
        ])
