# 🤖 MATIČÁK Chatbot - Integrace s Vertex AI

## 📋 Možnosti integrace s Google Vertex AI

### 🎯 Varianta 1: Vertex AI Agent Builder (Dialogflow CX)

**Výhody:**
- ✅ Nejjednodušší integrace - 1 řádek kódu
- ✅ Automatický hosting chatbota
- ✅ Built-in NLP a porozumění kontextu
- ✅ Žádný vlastní backend server
- ✅ Škálovatelnost zaručena Googlem

**Jak na to:**

#### 1. Vytvoř Dialogflow CX agenta
```bash
# V Google Cloud Console:
1. Přejdi na: https://console.cloud.google.com/
2. Aktivuj "Dialogflow API"
3. Vytvoř nový projekt: "maticak-chatbot"
4. Jdi do "Dialogflow CX" → "Create Agent"
```

#### 2. Konfiguruj intenty a odpovědi

**Intent: Jídelna**
```
Training phrases:
- "Co je dnes k obědu?"
- "Jídelní lístek"
- "Co mají v jídelně?"
- "Menu"

Response:
- Webhook call → Tvoje FastAPI endpoint
```

**Intent: Rozvrh**
```
Training phrases:
- "Jaký mám rozvrh?"
- "Rozvrh třídy KVA"
- "Kdy mám matematiku?"

Response:
- Webhook call → Tvoje FastAPI endpoint
```

#### 3. Integrace na web (1 řádek)

**Varianta A - Messenger integration:**
```html
<!-- Před </body> -->
<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  chat-icon="https://mgo.cz/logo.png"
  agent-id="TVUJ-AGENT-ID"
  language-code="cs"
  chat-title="MATIČÁK"
  intent="WELCOME"
  placeholder="Napiš svou zprávu...">
</df-messenger>

<style>
  df-messenger {
    --df-messenger-bot-message: #667eea;
    --df-messenger-button-titlebar-color: #667eea;
    --df-messenger-chat-background-color: #f5f5f5;
    --df-messenger-font-color: white;
    --df-messenger-send-icon: #667eea;
    --df-messenger-user-message: #667eea;
  }
</style>
```

**Varianta B - Custom UI s Vertex AI API:**
```html
<script>
// Komunikace s Vertex AI přes REST API
async function sendMessageToVertex(message) {
  const response = await fetch('https://dialogflow.googleapis.com/v3/projects/TVUJ-PROJECT/locations/europe-west1/agents/TVUJ-AGENT/sessions/SESSION_ID:detectIntent', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + accessToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      queryInput: {
        text: {
          text: message
        },
        languageCode: 'cs'
      }
    })
  });
  
  const result = await response.json();
  return result.queryResult.responseMessages;
}
</script>
```

---

### 🚀 Varianta 2: Vertex AI Generative AI (Gemini) - Pro pokročilé

**Použití Google Gemini modelu přímo:**

#### 1. Backend - Python s Vertex AI SDK

```python
# main.py - upravená verze s Vertex AI
from fastapi import FastAPI
from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

app = FastAPI()

# Inicializace Vertex AI
aiplatform.init(project="tvuj-project", location="europe-west1")
model = GenerativeModel("gemini-pro")

@app.post("/chat")
async def chat(message: str):
    """Chatbot endpoint používající Gemini"""
    
    # Systémový prompt s kontextem MGO
    context = """
    Jsi MATIČÁK - virtuální asistent Matičního gymnázia Ostrava.
    Pomáháš studentům s informacemi o škole, jídelně, rozvrhu a učitelích.
    
    Dostupné funkce:
    - Jídelna: /jidelna/dnesni-menu
    - Rozvrh: /rozvrh/{trida}
    - Učitelé: /kontakt/ucitele/{predmet}
    - Vedení: /kontakt/vedeni
    
    Odpovídej vždy přátelsky a profesionálně v češtině.
    """
    
    # Volání Gemini
    response = model.generate_content(
        f"{context}\n\nUživatel: {message}"
    )
    
    return {
        "response": response.text,
        "success": True
    }

# Zachováme původní endpointy pro data
@app.get("/jidelna/dnesni-menu")
async def get_dnesni_menu():
    # Tvůj původní kód
    pass
```

#### 2. Frontend integrace

```javascript
// Chatbot s Vertex AI Gemini
async function sendMessage() {
    const userMessage = document.getElementById('userInput').value;
    
    // Zobraz zprávu uživatele
    addUserMessage(userMessage);
    
    // Zavolej backend s Vertex AI
    const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userMessage})
    });
    
    const data = await response.json();
    
    // Zobraz odpověď AI
    addBotMessage(data.response);
}
```

---

### 🔧 Varianta 3: Hybrid - Vertex AI + Tvůj Backend

**Nejlepší z obou světů:**

1. **Vertex AI** - Pro konverzaci a porozumění
2. **Tvůj FastAPI** - Pro specifická data (jídelna, rozvrh)

```python
# main.py - hybrid přístup
from fastapi import FastAPI
from vertexai.preview.generative_models import GenerativeModel
import json

app = FastAPI()
model = GenerativeModel("gemini-pro")

@app.post("/chat")
async def chat_hybrid(message: str):
    """
    Kombinace Vertex AI pro konverzaci 
    + FastAPI endpointy pro data
    """
    
    # Systémový prompt s funkcemi
    context = """
    Jsi MATIČÁK. Máš přístup k těmto funkcím:
    
    1. get_menu() - Získá dnešní menu
    2. get_rozvrh(trida) - Získá rozvrh třídy
    3. get_ucitele(predmet) - Seznam učitelů předmětu
    
    Když uživatel chce jídelníček, zavolej get_menu().
    Když chce rozvrh, zeptej se na třídu a zavolej get_rozvrh().
    """
    
    # Zavolej Gemini
    response = model.generate_content(
        f"{context}\n\nUživatel: {message}"
    )
    
    ai_response = response.text
    
    # Detekuj, jestli AI chce zavolat funkci
    if "get_menu()" in ai_response:
        menu_data = await get_dnesni_menu()  # Tvůj endpoint
        return {
            "response": f"Dnes máme: {format_menu(menu_data)}",
            "type": "menu",
            "data": menu_data
        }
    
    elif "get_rozvrh" in ai_response:
        # Zpracuj rozvrh...
        pass
    
    else:
        # Běžná konverzace
        return {
            "response": ai_response,
            "type": "text"
        }
```

---

## 📊 Srovnání variant

| Vlastnost | Dialogflow CX | Gemini API | Hybrid |
|-----------|---------------|------------|--------|
| **Složitost** | ⭐ Snadné | ⭐⭐ Střední | ⭐⭐⭐ Pokročilé |
| **Cena** | 💰 Od $0.007/req | 💰💰 Od $0.00025/1K znaků | 💰💰 Kombinace |
| **Customizace** | ⭐⭐ Omezená | ⭐⭐⭐ Plná | ⭐⭐⭐ Plná |
| **Hosting** | ☁️ Google | 🖥️ Tvůj server | 🖥️ Tvůj server |
| **NLP kvalita** | ⭐⭐⭐ Vysoká | ⭐⭐⭐⭐ Nejvyšší | ⭐⭐⭐⭐ Nejvyšší |

---

## 🎯 Doporučení pro MGO

### Pro rychlé nasazení (1 den):
→ **Dialogflow CX** s Messenger integration

### Pro nejlepší AI (3-5 dní):
→ **Hybrid varianta** (Gemini + FastAPI)

### Pro full control (1 týden):
→ **Custom s Gemini API** + tvůj kompletní UI

---

## 💡 Konkrétní kroky pro start:

### Krok 1: Aktivuj Vertex AI
```bash
# V terminálu
gcloud auth login
gcloud config set project maticak-chatbot
gcloud services enable dialogflow.googleapis.com
gcloud services enable aiplatform.googleapis.com
```

### Krok 2: Instaluj dependencies
```bash
pip install google-cloud-aiplatform
pip install vertexai
pip install google-cloud-dialogflow-cx
```

### Krok 3: Vytvoř .env soubor
```bash
# .env
GOOGLE_CLOUD_PROJECT=maticak-chatbot
GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json
DIALOGFLOW_AGENT_ID=tvuj-agent-id
```

### Krok 4: Test integrace
```python
# test_vertex.py
from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel

aiplatform.init(project="maticak-chatbot", location="europe-west1")
model = GenerativeModel("gemini-pro")

response = model.generate_content("Ahoj, jsem student MGO. Co je dnes k obědu?")
print(response.text)
```

---

## 🔗 Užitečné odkazy

- **Vertex AI Console**: https://console.cloud.google.com/vertex-ai
- **Dialogflow CX**: https://cloud.google.com/dialogflow/cx/docs
- **Gemini API**: https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini
- **Pricing**: https://cloud.google.com/vertex-ai/pricing

---

## ❓ Máš další otázky?

1. Chceš vidět kompletní implementaci s Vertex AI?
2. Mám připravit konfiguraci pro Dialogflow CX?
3. Nebo vytvoříme hybrid řešení s Gemini?

**Dej vědět, kterou variantu preferuješ!** 🚀
