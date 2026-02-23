// MATY Chatbot Widget - Kompletní implementace
// Použití: <script src="chatbot-embed.js"></script> na konci stránky

(function() {
    'use strict';
    
    // Načtení config.js
    const configScript = document.createElement('script');
    configScript.src = 'config.js';
    document.head.appendChild(configScript);
    
    // Vložení CSS stylů pro chatbot
    const style = document.createElement('style');
    style.textContent = `
        /* Reset a základní styly pro chatbot */
        #maty-chatbot-widget * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Hlavní kontejner chatbota */
        #maty-chatbot-container {
            position: fixed;
            bottom: 24px;
            right: 24px;
            width: 400px;
            height: 600px;
            background: white;
            border-radius: 24px;
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);
            display: none;
            flex-direction: column;
            overflow: hidden;
            z-index: 999999;
            border: 1px solid rgba(0, 0, 0, 0.08);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        }

        #maty-chatbot-container.show {
            display: flex;
        }

        /* Tlačítko pro otevření/zavření */
        #maty-chat-toggle {
            position: fixed;
            bottom: 24px;
            right: 24px;
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, #5B6FE8 0%, #7C4DFF 100%);
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 30px;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(91,111,232,0.35);
            z-index: 999998;
            transition: all 0.3s;
            border: 2px solid rgba(255,255,255,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #maty-chat-toggle:hover {
            transform: scale(1.08) translateY(-2px);
            box-shadow: 0 12px 32px rgba(91,111,232,0.45);
        }

        /* Hlavička */
        .maty-header {
            background: linear-gradient(135deg, #5B6FE8 0%, #7C4DFF 100%);
            color: white;
            padding: 20px 24px;
            text-align: left;
            position: relative;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .maty-header h1 {
            font-size: 22px;
            margin-bottom: 4px;
            font-weight: 600;
            letter-spacing: -0.3px;
        }

        .maty-header p {
            font-size: 13px;
            opacity: 0.85;
            font-weight: 400;
        }

        /* Tlačítko zavřít */
        .maty-close-btn {
            position: absolute;
            top: 16px;
            right: 16px;
            background: rgba(255, 255, 255, 0.2);
            border: none;
            color: white;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .maty-close-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: rotate(90deg);
        }

        /* Novinky badge */
        .maty-novinka-badge {
            position: absolute;
            top: 10px;
            right: 55px;
            background: white;
            color: #333;
            padding: 6px 12px;
            border-radius: 18px;
            font-size: 10px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 4px;
            box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
            animation: blinkBadge 2s ease-in-out infinite, floatBubble 3s ease-in-out infinite;
            transition: all 0.3s ease;
            z-index: 1000;
            border: 2px solid #ff6b6b;
        }

        .maty-novinka-badge::after {
            content: '';
            position: absolute;
            bottom: -8px;
            right: 25%;
            width: 0;
            height: 0;
            border-left: 6px solid transparent;
            border-right: 6px solid transparent;
            border-top: 8px solid white;
        }

        @keyframes blinkBadge {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }

        @keyframes floatBubble {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }

        /* Kontejner pro zprávy */
        .maty-chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background: #F5F5F7;
        }

        .maty-chat-container::-webkit-scrollbar {
            width: 6px;
        }

        .maty-chat-container::-webkit-scrollbar-thumb {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        }

        /* Zprávy */
        .maty-message {
            margin-bottom: 16px;
            display: flex;
            align-items: flex-start;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .maty-message.user {
            justify-content: flex-end;
        }

        .maty-message-content {
            max-width: 75%;
            padding: 12px 16px;
            border-radius: 18px;
            line-height: 1.5;
            font-size: 14px;
            word-wrap: break-word;
        }

        .maty-message.bot .maty-message-content {
            background: white;
            color: #333;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .maty-message.user .maty-message-content {
            background: linear-gradient(135deg, #5B6FE8 0%, #7C4DFF 100%);
            color: white;
        }

        /* Input kontejner */
        .maty-input-container {
            padding: 16px;
            background: white;
            border-top: 1px solid #E8E8EA;
            display: flex;
            gap: 10px;
        }

        #maty-userInput {
            flex: 1;
            padding: 12px 16px;
            border: 1.5px solid #E8E8EA;
            border-radius: 24px;
            font-size: 14px;
            outline: none;
            transition: all 0.3s ease;
            background: #F5F5F7;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        #maty-userInput:focus {
            border-color: #5B6FE8;
            background: white;
            box-shadow: 0 0 0 3px rgba(91, 111, 232, 0.1);
        }

        #maty-sendBtn {
            padding: 10px 20px;
            background: linear-gradient(135deg, #5B6FE8 0%, #7C4DFF 100%);
            color: white;
            border: none;
            border-radius: 24px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 2px 8px rgba(91, 111, 232, 0.25);
        }

        #maty-sendBtn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(91, 111, 232, 0.4);
        }

        #maty-sendBtn:active {
            transform: scale(0.96);
        }

        #maty-sendBtn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }

        /* Responsivní styly */
        @media screen and (max-width: 768px) {
            #maty-chatbot-container {
                bottom: 0;
                right: 5%;
                left: 5%;
                width: 90%;
                height: 70vh;
                max-height: 600px;
                border-radius: 20px 20px 0 0;
            }

            #maty-chat-toggle {
                width: 60px;
                height: 60px;
                font-size: 28px;
                bottom: 15px;
                right: 15px;
            }

            #maty-sendBtn {
                padding: 8px 14px;
                font-size: 13px;
                min-width: 65px;
            }
        }

        @media screen and (max-width: 480px) {
            #maty-chatbot-container {
                left: 5%;
                right: 5%;
                width: 90%;
                height: 75vh;
                max-height: none;
                border-radius: 15px 15px 0 0;
            }

            #maty-sendBtn {
                padding: 8px 12px;
                font-size: 12px;
                min-width: 60px;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Vytvoření HTML struktury
    const chatHTML = `
        <button id="maty-chat-toggle">💬</button>
        
        <div id="maty-chatbot-container">
            <div class="maty-header">
                <h1>MATY</h1>
                <p>Tvůj AI pomocník</p>
                <div class="maty-novinka-badge">
                    🔥 NOVINKY
                </div>
                <button class="maty-close-btn">✕</button>
            </div>
            
            <div class="maty-chat-container" id="maty-chatMessages">
                <div class="maty-message bot">
                    <div class="maty-message-content">
                        Ahoj! 👋 Jsem MATY, tvůj AI asistent pro Matiční gymnázium. Jak ti mohu pomoci?
                    </div>
                </div>
            </div>
            
            <div class="maty-input-container">
                <input type="text" id="maty-userInput" placeholder="Napiš svou zprávu..." autocomplete="off">
                <button id="maty-sendBtn">Odeslat</button>
            </div>
        </div>
    `;
    
    // Vložení do stránky
    const widgetContainer = document.createElement('div');
    widgetContainer.id = 'maty-chatbot-widget';
    widgetContainer.innerHTML = chatHTML;
    document.body.appendChild(widgetContainer);
    
    // JavaScript logika
    let chatOpen = false;
    const container = document.getElementById('maty-chatbot-container');
    const toggleBtn = document.getElementById('maty-chat-toggle');
    const closeBtn = document.querySelector('.maty-close-btn');
    const userInput = document.getElementById('maty-userInput');
    const sendBtn = document.getElementById('maty-sendBtn');
    const chatMessages = document.getElementById('maty-chatMessages');
    
    // Toggle chatbot
    function toggleChat() {
        chatOpen = !chatOpen;
        if (chatOpen) {
            container.classList.add('show');
            toggleBtn.style.display = 'none';
            userInput.focus();
        } else {
            container.classList.remove('show');
            toggleBtn.style.display = 'flex';
        }
    }
    
    toggleBtn.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);
    
    // Odeslání zprávy
    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        
        // Přidat uživatelskou zprávu
        const userMsg = document.createElement('div');
        userMsg.className = 'maty-message user';
        userMsg.innerHTML = `<div class="maty-message-content">${escapeHtml(message)}</div>`;
        chatMessages.appendChild(userMsg);
        
        userInput.value = '';
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Zakázat tlačítko během načítání
        sendBtn.disabled = true;
        
        // Volání API
        fetch(window.BACKEND_URL + '/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            const botMsg = document.createElement('div');
            botMsg.className = 'maty-message bot';
            botMsg.innerHTML = `<div class="maty-message-content">${escapeHtml(data.response || 'Omlouv ám se, něco se pokazilo.')}</div>`;
            chatMessages.appendChild(botMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        })
        .catch(error => {
            console.error('Chyba při komunikaci s API:', error);
            const errorMsg = document.createElement('div');
            errorMsg.className = 'maty-message bot';
            errorMsg.innerHTML = `<div class="maty-message-content">Omlouvám se, nepodařilo se mi spojit se serverem.</div>`;
            chatMessages.appendChild(errorMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        })
        .finally(() => {
            sendBtn.disabled = false;
        });
    }
    
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    // Helper funkce pro escapování HTML
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // Automatické otevření pokud je v URL ?openChat=true
    if (window.location.search.includes('openChat=true')) {
        setTimeout(() => {
            toggleChat();
        }, 500);
    }
    
})();
