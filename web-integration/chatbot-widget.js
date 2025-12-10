/**
 * MATIČÁK Chatbot Widget - Standalone verze pro integraci na webové stránky
 * Verze: 1.0
 * Autor: Žáci Matičního gymnázia Ostrava
 * 
 * POUŽITÍ:
 * 1. Nahraj tento soubor na svůj web server
 * 2. Přidej do HTML před </body>:
 *    <script src="chatbot-widget.js"></script>
 *    <script>
 *      MaticakChatbot.init({
 *        apiUrl: 'http://tvoje-server-adresa:8000'
 *      });
 *    </script>
 */

(function(window) {
    'use strict';
    
    const MaticakChatbot = {
        // Konfigurace
        config: {
            apiUrl: window.location.origin,
            containerZIndex: 999999,
            buttonZIndex: 999998
        },
        
        // Inicializace chatbota
        init: function(options) {
            // Přepis výchozí konfigurace
            if (options && options.apiUrl) {
                this.config.apiUrl = options.apiUrl;
            }
            
            // Vložení CSS stylů
            this.injectStyles();
            
            // Vložení HTML struktury
            this.injectHTML();
            
            // Inicializace event listenerů
            this.initEventListeners();
            
            console.log('✅ MATIČÁK Chatbot inicializován', this.config);
        },
        
        // Vložení CSS stylů do stránky
        injectStyles: function() {
            const style = document.createElement('style');
            style.textContent = `
                /* MATIČÁK Chatbot Styles */
                #maticak-chatbot-container {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    width: 320px;
                    height: 480px;
                    background: white;
                    border-radius: 5px;
                    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.3);
                    display: flex;
                    flex-direction: column;
                    overflow: hidden;
                    z-index: ${this.config.containerZIndex};
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    transform: translateY(600px);
                    opacity: 0;
                    pointer-events: none;
                    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                }
                
                #maticak-chatbot-container.active {
                    transform: translateY(0);
                    opacity: 1;
                    pointer-events: all;
                }
                
                #maticak-chat-toggle-btn {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    width: 60px;
                    height: 60px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    border-radius: 50%;
                    font-size: 28px;
                    cursor: pointer;
                    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.6);
                    z-index: ${this.config.buttonZIndex};
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: all 0.3s ease;
                    animation: pulse 2s infinite;
                }
                
                #maticak-chat-toggle-btn:hover {
                    transform: scale(1.1);
                    box-shadow: 0 6px 30px rgba(102, 126, 234, 0.8);
                }
                
                @keyframes pulse {
                    0% { box-shadow: 0 2px 10px rgba(102, 126, 234, 0.6); }
                    50% { box-shadow: 0 2px 15px rgba(102, 126, 234, 0.9), 0 0 0 5px rgba(102, 126, 234, 0.1); }
                    100% { box-shadow: 0 2px 10px rgba(102, 126, 234, 0.6); }
                }
                
                #maticak-chatbot-header {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 10px 16px;
                    text-align: center;
                }
                
                #maticak-chatbot-header h1 {
                    font-size: 18px;
                    margin: 0 0 2px 0;
                    font-style: italic;
                }
                
                #maticak-chatbot-header p {
                    font-size: 9px;
                    margin: 0;
                    opacity: 0.9;
                }
                
                #maticak-chat-messages {
                    flex: 1;
                    overflow-y: auto;
                    padding: 16px;
                    background: #f5f5f5;
                }
                
                .maticak-quick-buttons {
                    position: sticky;
                    top: 0;
                    background: linear-gradient(to bottom, #f5f5f5 0%, #f5f5f5 85%, rgba(245, 245, 245, 0) 100%);
                    padding: 8px 16px 12px 16px;
                    margin: -16px -16px 8px -16px;
                    display: flex;
                    gap: 8px;
                    justify-content: center;
                    z-index: 100;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                }
                
                .maticak-quick-btn {
                    padding: 5px 10px;
                    background: white;
                    color: #667eea;
                    border: 2px solid #667eea;
                    border-radius: 3px;
                    font-size: 9px;
                    font-weight: 600;
                    cursor: pointer;
                    transition: all 0.3s;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
                    white-space: nowrap;
                }
                
                .maticak-quick-btn:hover {
                    background: #667eea;
                    color: white;
                    transform: translateY(-2px);
                }
                
                .maticak-message {
                    margin-bottom: 15px;
                    display: flex;
                    animation: fadeIn 0.3s ease-in;
                }
                
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                
                .maticak-message.user {
                    justify-content: flex-end;
                }
                
                .maticak-message-content {
                    max-width: 70%;
                    padding: 10px 14px;
                    border-radius: 3px;
                    word-wrap: break-word;
                    white-space: pre-wrap;
                    font-size: 10px;
                }
                
                .maticak-message.user .maticak-message-content {
                    background: #667eea;
                    color: white;
                }
                
                .maticak-message.bot .maticak-message-content {
                    background: white;
                    color: #333;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }
                
                #maticak-chat-input-container {
                    padding: 8px 12px;
                    background: white;
                    border-top: 1px solid #e0e0e0;
                    display: flex;
                    gap: 6px;
                }
                
                #maticak-chat-input {
                    flex: 1;
                    padding: 6px 10px;
                    border: 2px solid #e0e0e0;
                    border-radius: 3px;
                    font-size: 11px;
                    outline: none;
                    transition: border-color 0.3s;
                    font-family: inherit;
                }
                
                #maticak-chat-input:focus {
                    border-color: #667eea;
                }
                
                #maticak-chat-send-btn {
                    padding: 6px 16px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    border-radius: 3px;
                    font-size: 11px;
                    cursor: pointer;
                    transition: transform 0.2s;
                }
                
                #maticak-chat-send-btn:hover {
                    transform: translateY(-2px);
                }
                
                #maticak-chatbot-footer {
                    padding: 6px 12px;
                    text-align: center;
                    font-size: 7px;
                    color: #999;
                    background: white;
                    border-top: 1px solid #e0e0e0;
                }
                
                /* Modaly */
                .maticak-modal {
                    display: none;
                    position: fixed;
                    z-index: ${this.config.containerZIndex + 10};
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.5);
                }
                
                .maticak-modal.active {
                    display: block;
                }
                
                .maticak-modal-content {
                    background-color: white;
                    margin: 5% auto;
                    padding: 20px;
                    border-radius: 12px;
                    width: 400px;
                    max-width: 90%;
                    max-height: 500px;
                    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
                    overflow-y: auto;
                }
                
                .maticak-modal-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 12px;
                }
                
                .maticak-modal-header h2 {
                    color: #667eea;
                    font-size: 18px;
                    margin: 0;
                }
                
                .maticak-modal-close {
                    background: none;
                    border: none;
                    font-size: 24px;
                    color: #999;
                    cursor: pointer;
                    padding: 0;
                    width: 24px;
                    height: 24px;
                }
                
                .maticak-modal-close:hover {
                    color: #333;
                }
                
                .maticak-modal-body {
                    color: #333;
                    font-size: 13px;
                    line-height: 1.6;
                }
                
                /* Responzivní design */
                @media screen and (max-width: 768px) {
                    #maticak-chatbot-container {
                        bottom: 0;
                        right: 0;
                        left: 0;
                        width: 100%;
                        height: 70vh;
                        border-radius: 20px 20px 0 0;
                    }
                    
                    #maticak-chatbot-container.active {
                        transform: translateY(0);
                    }
                    
                    #maticak-chat-toggle-btn {
                        width: 70px;
                        height: 70px;
                        font-size: 32px;
                    }
                }
            `;
            document.head.appendChild(style);
        },
        
        // Vložení HTML struktury
        injectHTML: function() {
            const html = `
                <!-- MATIČÁK Chatbot Toggle Button -->
                <button id="maticak-chat-toggle-btn" aria-label="Otevřít chatbot">
                    💬
                </button>
                
                <!-- MATIČÁK Chatbot Container -->
                <div id="maticak-chatbot-container">
                    <div id="maticak-chatbot-header">
                        <h1>🤖 MATIČÁK</h1>
                        <p>Matiční AI Pomocník</p>
                    </div>
                    
                    <div id="maticak-chat-messages">
                        <div class="maticak-quick-buttons">
                            <button class="maticak-quick-btn" data-action="kontakt">📧 Kontakt</button>
                            <button class="maticak-quick-btn" data-action="jidelna">🍽️ Jídelna</button>
                            <button class="maticak-quick-btn" data-action="rozvrh">📅 Rozvrh</button>
                        </div>
                    </div>
                    
                    <div id="maticak-chat-input-container">
                        <input type="text" id="maticak-chat-input" placeholder="Napiš svou zprávu..." autocomplete="off">
                        <button id="maticak-chat-send-btn">Odeslat</button>
                    </div>
                    
                    <div id="maticak-chatbot-footer">
                        Vytvořili žáci Matičního gymnázia Ostrava
                    </div>
                </div>
                
                <!-- Modal pro Kontakt -->
                <div id="maticak-kontakt-modal" class="maticak-modal">
                    <div class="maticak-modal-content">
                        <div class="maticak-modal-header">
                            <h2>📧 Kontakt</h2>
                            <button class="maticak-modal-close" data-modal="kontakt">&times;</button>
                        </div>
                        <div class="maticak-modal-body" id="maticak-kontakt-body">
                            <p>⏳ Načítám kontaktní informace...</p>
                        </div>
                    </div>
                </div>
                
                <!-- Modal pro Jídelnu -->
                <div id="maticak-jidelna-modal" class="maticak-modal">
                    <div class="maticak-modal-content">
                        <div class="maticak-modal-header">
                            <h2>🍽️ Jídelna</h2>
                            <button class="maticak-modal-close" data-modal="jidelna">&times;</button>
                        </div>
                        <div class="maticak-modal-body" id="maticak-jidelna-body">
                            <p>⏳ Načítám dnešní menu...</p>
                        </div>
                    </div>
                </div>
                
                <!-- Modal pro Rozvrh -->
                <div id="maticak-rozvrh-modal" class="maticak-modal">
                    <div class="maticak-modal-content">
                        <div class="maticak-modal-header">
                            <h2>📅 Rozvrh</h2>
                            <button class="maticak-modal-close" data-modal="rozvrh">&times;</button>
                        </div>
                        <div class="maticak-modal-body" id="maticak-rozvrh-body">
                            <h3>Vyber třídu:</h3>
                            <p>Funkce rozvrhu - v implementaci...</p>
                        </div>
                    </div>
                </div>
            `;
            
            document.body.insertAdjacentHTML('beforeend', html);
        },
        
        // Inicializace event listenerů
        initEventListeners: function() {
            const self = this;
            
            // Toggle button
            const toggleBtn = document.getElementById('maticak-chat-toggle-btn');
            const container = document.getElementById('maticak-chatbot-container');
            
            toggleBtn.addEventListener('click', function() {
                container.classList.toggle('active');
            });
            
            // Quick action buttons
            const quickBtns = document.querySelectorAll('.maticak-quick-btn');
            quickBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    const action = this.getAttribute('data-action');
                    self.handleQuickAction(action);
                });
            });
            
            // Send button
            const sendBtn = document.getElementById('maticak-chat-send-btn');
            const input = document.getElementById('maticak-chat-input');
            
            sendBtn.addEventListener('click', function() {
                self.sendMessage();
            });
            
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    self.sendMessage();
                }
            });
            
            // Modal close buttons
            const closeButtons = document.querySelectorAll('.maticak-modal-close');
            closeButtons.forEach(btn => {
                btn.addEventListener('click', function() {
                    const modalName = this.getAttribute('data-modal');
                    self.closeModal(modalName);
                });
            });
            
            // Close modal on outside click
            const modals = document.querySelectorAll('.maticak-modal');
            modals.forEach(modal => {
                modal.addEventListener('click', function(e) {
                    if (e.target === this) {
                        this.classList.remove('active');
                    }
                });
            });
            
            // Show welcome message
            setTimeout(() => {
                this.addBotMessage('👋 Ahoj! Jsem MATIČÁK - virtuální asistent Matičního gymnázia.\n\nJak ti mohu pomoci?');
            }, 500);
        },
        
        // Zpracování quick action tlačítek
        handleQuickAction: function(action) {
            switch(action) {
                case 'kontakt':
                    this.showKontakt();
                    break;
                case 'jidelna':
                    this.showJidelna();
                    break;
                case 'rozvrh':
                    this.showRozvrh();
                    break;
            }
        },
        
        // Zobrazení kontaktu
        showKontakt: function() {
            const modal = document.getElementById('maticak-kontakt-modal');
            const body = document.getElementById('maticak-kontakt-body');
            
            modal.classList.add('active');
            body.innerHTML = `
                <h3>Matiční gymnázium Ostrava</h3>
                <p><strong>📧 E-mail:</strong> <a href="mailto:info@mgo.cz">info@mgo.cz</a></p>
                <p><strong>🌐 Web:</strong> <a href="https://mgo.cz" target="_blank">mgo.cz</a></p>
                <p><strong>📞 Telefon:</strong> <a href="tel:+420596116239">+420 596 11 62 39</a></p>
            `;
        },
        
        // Zobrazení jídelny
        showJidelna: async function() {
            const modal = document.getElementById('maticak-jidelna-modal');
            const body = document.getElementById('maticak-jidelna-body');
            
            modal.classList.add('active');
            body.innerHTML = '<p>⏳ Načítám dnešní menu...</p>';
            
            try {
                const response = await fetch(`${this.config.apiUrl}/jidelna/dnesni-menu`);
                const result = await response.json();
                
                if (result.success && result.data) {
                    let html = `<h3>🍽️ Dnešní menu - ${result.data.den} ${result.data.datum}</h3>`;
                    
                    if (result.data.menu && result.data.menu.length > 0) {
                        result.data.menu.forEach(jidlo => {
                            html += `<p><strong>${jidlo.typ}:</strong><br>${jidlo.nazev}</p>`;
                        });
                    } else {
                        html += '<p>Dnes není k dispozici žádné menu.</p>';
                    }
                    
                    body.innerHTML = html;
                } else {
                    body.innerHTML = '<p style="color: red;">❌ Nepodařilo se načíst dnešní menu.</p>';
                }
            } catch (error) {
                console.error('Chyba při načítání menu:', error);
                body.innerHTML = '<p style="color: red;">❌ Došlo k chybě při načítání menu.</p>';
            }
        },
        
        // Zobrazení rozvrhu
        showRozvrh: function() {
            const modal = document.getElementById('maticak-rozvrh-modal');
            modal.classList.add('active');
        },
        
        // Zavření modalu
        closeModal: function(modalName) {
            const modal = document.getElementById(`maticak-${modalName}-modal`);
            modal.classList.remove('active');
        },
        
        // Odeslání zprávy
        sendMessage: function() {
            const input = document.getElementById('maticak-chat-input');
            const message = input.value.trim();
            
            if (message === '') return;
            
            // Přidat uživatelskou zprávu
            this.addUserMessage(message);
            
            // Vyčistit input
            input.value = '';
            
            // Simulace odpovědi (zde by bylo volání API)
            setTimeout(() => {
                this.addBotMessage('Omlouvám se, tato funkce je ve vývoji. Použij prosím rychlá tlačítka nahoře. 😊');
            }, 500);
        },
        
        // Přidat zprávu uživatele
        addUserMessage: function(text) {
            const messagesContainer = document.getElementById('maticak-chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'maticak-message user';
            messageDiv.innerHTML = `<div class="maticak-message-content">${this.escapeHtml(text)}</div>`;
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        },
        
        // Přidat zprávu bota
        addBotMessage: function(text) {
            const messagesContainer = document.getElementById('maticak-chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'maticak-message bot';
            messageDiv.innerHTML = `<div class="maticak-message-content">${this.escapeHtml(text)}</div>`;
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        },
        
        // Escape HTML pro bezpečnost
        escapeHtml: function(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    };
    
    // Export do globálního scope
    window.MaticakChatbot = MaticakChatbot;
    
})(window);
