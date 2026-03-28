/**
 * MATIČÁK Chatbot Widget - Iframe verze pro integraci na webové stránky
 * Verze: 3.0
 * Autor: Žáci Matičního gymnázia Ostrava
 * 
 * POUŽITÍ:
 * 1. Přidej tento soubor na svůj web
 * 2. Přidej do HTML před </body>:
 *    <script src="chatbot-widget-v2.js"></script>
 *    <script>MaticakChatbot.init();</script>
 */

(function(window) {
    'use strict';
    
    const MaticakChatbot = {
        config: {
            chatbotUrl: 'https://tmutina79-png.github.io/chatbot-rag-ready/chat.html',
            width: '400px',
            height: '600px',
            position: {
                bottom: '24px',
                right: '24px'
            }
        },
        
        isOpen: false,
        iframeLoaded: false,
        modalCloseTimeout: null,
        
        init: function(options) {
            if (options) {
                Object.assign(this.config, options);
            }
            this.injectStyles();
            this.injectHTML();
            this.initEventListeners();
            this.showGreeting();
            console.log('✅ MATIČÁK Chatbot v3.0 načten');
        },
        
        injectStyles: function() {
            const style = document.createElement('style');
            style.textContent = '\
                #maticak-chatbot-iframe {\
                    position: fixed;\
                    bottom: ' + this.config.position.bottom + ';\
                    right: ' + this.config.position.right + ';\
                    width: ' + this.config.width + ';\
                    height: ' + this.config.height + ';\
                    border: none;\
                    border-radius: 24px;\
                    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);\
                    z-index: 999999;\
                    visibility: hidden;\
                    opacity: 0;\
                    pointer-events: none;\
                    transition: opacity 0.3s ease, visibility 0.3s ease;\
                }\
                #maticak-chatbot-iframe.maticak-visible {\
                    visibility: visible;\
                    opacity: 1;\
                    pointer-events: auto;\
                }\
                #maticak-chat-toggle {\
                    position: fixed;\
                    top: 160px;\
                    right: 10px;\
                    width: auto;\
                    height: auto;\
                    background: transparent;\
                    color: white;\
                    border: none;\
                    border-radius: 0;\
                    font-size: 30px;\
                    cursor: pointer;\
                    box-shadow: none;\
                    z-index: 9999999;\
                    transition: transform 0.3s ease, filter 0.3s ease, opacity 0.3s ease;\
                    display: block;\
                    padding: 0;\
                    animation: maticakFloat 3s ease-in-out infinite;\
                    filter: drop-shadow(0 6px 20px rgba(0, 0, 0, 0.35));\
                    pointer-events: auto;\
                    -webkit-tap-highlight-color: transparent;\
                }\
                #maticak-chat-toggle img {\
                    width: 140px;\
                    height: auto;\
                    display: block;\
                    object-fit: contain;\
                    background: transparent;\
                    pointer-events: none;\
                }\
                #maticak-chat-toggle:hover {\
                    transform: scale(1.08);\
                    filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.5));\
                    animation-play-state: paused;\
                }\
                #maticak-chat-toggle:active {\
                    transform: scale(0.95);\
                }\
                #maticak-chat-toggle.maticak-hidden {\
                    display: none;\
                }\
                #maticak-greeting-bubble {\
                    position: fixed;\
                    top: 310px;\
                    right: 24px;\
                    background: white;\
                    color: #1D1D1F;\
                    padding: 12px 18px;\
                    border-radius: 16px 16px 4px 16px;\
                    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;\
                    font-size: 14px;\
                    font-weight: 500;\
                    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);\
                    z-index: 999997;\
                    animation: maticakBubbleIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), maticakPulseGlow 1.5s ease-in-out 0.5s infinite;\
                    cursor: pointer;\
                    max-width: 220px;\
                    line-height: 1.4;\
                }\
                #maticak-chat-toggle.maticak-pulse {\
                    animation: maticakTogglePulse 1.2s ease-in-out infinite;\
                }\
                #maticak-greeting-bubble.maticak-bubble-out {\
                    animation: maticakBubbleOut 0.3s ease forwards;\
                }\
                @keyframes maticakBubbleIn {\
                    from { opacity: 0; transform: translateY(10px) scale(0.9); }\
                    to { opacity: 1; transform: translateY(0) scale(1); }\
                }\
                @keyframes maticakBubbleOut {\
                    from { opacity: 1; transform: translateY(0) scale(1); }\
                    to { opacity: 0; transform: translateY(10px) scale(0.9); }\
                }\
                @keyframes maticakPulseGlow {\
                    0%, 100% { box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15); transform: scale(1); }\
                    50% { box-shadow: 0 8px 30px rgba(0, 106, 172, 0.4); transform: scale(1.03); }\
                }\
                @keyframes maticakTogglePulse {\
                    0%, 100% { transform: scale(1); }\
                    50% { transform: scale(1.08); }\
                }\
                @keyframes maticakFloat {\
                    0%, 100% { transform: translateY(0px); }\
                    50% { transform: translateY(-10px); }\
                }\
                #maticak-modal-overlay {\
                    position: fixed;\
                    top: 0;\
                    left: 0;\
                    width: 100%;\
                    height: 100%;\
                    background: rgba(0, 0, 0, 0.35);\
                    z-index: 9999999;\
                    display: flex;\
                    align-items: center;\
                    justify-content: center;\
                    animation: maticakFadeIn 0.3s ease;\
                }\
                @keyframes maticakFadeIn {\
                    from { opacity: 0; }\
                    to { opacity: 1; }\
                }\
                #maticak-modal-wrapper {\
                    background: white;\
                    border-radius: 24px;\
                    width: 500px;\
                    max-width: 90%;\
                    max-height: 80vh;\
                    overflow-y: auto;\
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);\
                    animation: maticakSlideUp 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);\
                    position: relative;\
                    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;\
                }\
                #maticak-modal-wrapper * { box-sizing: border-box; }\
                #maticak-modal-wrapper .modal-content {\
                    padding: 24px;\
                    display: flex;\
                    flex-direction: column;\
                }\
                #maticak-modal-wrapper .modal-header {\
                    display: flex;\
                    justify-content: space-between;\
                    align-items: center;\
                    margin-bottom: 0;\
                    padding: 16px 24px;\
                    border-bottom: none;\
                    background: linear-gradient(135deg, #006aac 0%, #0a78b0 100%);\
                    border-radius: 24px 24px 0 0;\
                    margin: -24px -24px 20px -24px;\
                }\
                #maticak-modal-wrapper .modal-header h2 {\
                    color: #ffffff;\
                    font-size: 24px;\
                    font-weight: 600;\
                    margin: 0;\
                    letter-spacing: -0.5px;\
                }\
                #maticak-modal-wrapper .close-btn {\
                    background: rgba(255, 255, 255, 0.2);\
                    border: none;\
                    font-size: 20px;\
                    color: #ffffff;\
                    cursor: pointer;\
                    padding: 0;\
                    width: 32px;\
                    height: 32px;\
                    display: flex;\
                    align-items: center;\
                    justify-content: center;\
                    transition: all 0.2s ease;\
                    border-radius: 50%;\
                }\
                #maticak-modal-wrapper .close-btn:hover {\
                    background: rgba(255, 255, 255, 0.35);\
                    color: #ffffff;\
                    transform: scale(1.05);\
                }\
                #maticak-modal-wrapper .modal-body {\
                    color: #1D1D1F;\
                    font-size: 15px;\
                    line-height: 1.6;\
                }\
                #maticak-modal-wrapper .modal-body h3 {\
                    color: #1D1D1F;\
                    font-size: 18px;\
                    font-weight: 600;\
                    margin: 20px 0 12px 0;\
                    letter-spacing: -0.3px;\
                }\
                #maticak-modal-wrapper .modal-body h4 {\
                    margin: 15px 0 8px 0;\
                    font-size: 14px;\
                }\
                #maticak-modal-wrapper .modal-body p {\
                    margin: 12px 0;\
                    color: #494949;\
                }\
                #maticak-modal-wrapper .modal-body a {\
                    color: #006aac;\
                    text-decoration: none;\
                    transition: all 0.2s ease;\
                    font-weight: 500;\
                }\
                #maticak-modal-wrapper .modal-body a:hover {\
                    color: #0a78b0;\
                }\
                #maticak-modal-wrapper .info-section {\
                    margin-bottom: 24px;\
                    padding-bottom: 20px;\
                    border-bottom: 1px solid #E8E8EA;\
                }\
                #maticak-modal-wrapper .info-section:last-child {\
                    border-bottom: none;\
                    margin-bottom: 0;\
                }\
                #maticak-modal-wrapper .button-grid {\
                    display: grid;\
                    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));\
                    gap: 12px;\
                    margin-top: 16px;\
                }\
                #maticak-modal-wrapper .info-link-btn {\
                    display: flex;\
                    align-items: center;\
                    justify-content: center;\
                    padding: 14px 20px;\
                    background: linear-gradient(135deg, #006aac 0%, #0a78b0 100%);\
                    color: white !important;\
                    border: none;\
                    border-radius: 16px;\
                    font-size: 14px;\
                    font-weight: 600;\
                    text-decoration: none !important;\
                    text-align: center;\
                    cursor: pointer;\
                    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);\
                    box-shadow: 0 4px 12px rgba(0, 106, 172, 0.3);\
                    min-height: 52px;\
                }\
                #maticak-modal-wrapper .info-link-btn:hover {\
                    transform: translateY(-3px);\
                    box-shadow: 0 6px 20px rgba(0, 106, 172, 0.4);\
                    background: linear-gradient(135deg, #005284 0%, #0080cc 100%);\
                }\
                #maticak-modal-wrapper .contact-links {\
                    display: flex;\
                    flex-direction: column;\
                    gap: 8px;\
                    margin-top: 12px;\
                }\
                #maticak-modal-wrapper .contact-link {\
                    display: block;\
                    padding: 10px 14px;\
                    background: transparent;\
                    color: #0080cc;\
                    text-decoration: none;\
                    border: 1.5px solid #0080cc;\
                    border-radius: 6px;\
                    text-align: center;\
                    transition: all 0.3s;\
                    font-size: 13px;\
                }\
                #maticak-modal-wrapper .contact-link:hover {\
                    background: #0080cc !important;\
                    color: white !important;\
                    transform: translateY(-1px);\
                }\
                #maticak-modal-wrapper .tridy-grid {\
                    display: flex;\
                    flex-wrap: wrap;\
                    gap: 8px;\
                    margin-top: 5px;\
                    align-items: center;\
                }\
                #maticak-modal-wrapper .trida-btn {\
                    padding: 8px;\
                    background: transparent;\
                    color: #0080cc;\
                    border: 1px solid #0080cc;\
                    border-radius: 6px;\
                    font-size: 13px;\
                    font-weight: 600;\
                    cursor: pointer;\
                    transition: all 0.3s;\
                    text-align: center;\
                    min-width: 50px;\
                    height: 40px;\
                    display: inline-flex;\
                    align-items: center;\
                    justify-content: center;\
                }\
                #maticak-modal-wrapper .trida-btn:hover {\
                    background: #0080cc;\
                    color: white;\
                    transform: translateY(-2px);\
                    box-shadow: 0 4px 15px rgba(0, 106, 172, 0.4);\
                }\
                #maticak-modal-wrapper .trida-btn[title] {\
                    position: relative;\
                }\
                #maticak-modal-wrapper .trida-btn[title]:hover::after {\
                    content: attr(title);\
                    position: absolute;\
                    bottom: 100%;\
                    left: 50%;\
                    transform: translateX(-50%);\
                    margin-bottom: 5px;\
                    padding: 6px 10px;\
                    background: #333;\
                    color: white;\
                    font-size: 11px;\
                    white-space: nowrap;\
                    border-radius: 4px;\
                    z-index: 1000;\
                    pointer-events: none;\
                }\
                #maticak-modal-wrapper .predmet-btn {\
                    display: inline-block;\
                    margin: 5px;\
                    padding: 8px 16px;\
                    background: transparent;\
                    color: #0080cc;\
                    text-decoration: none;\
                    border: 2px solid #0080cc;\
                    border-radius: 20px;\
                    font-size: 11px;\
                    cursor: pointer;\
                    transition: all 0.3s;\
                }\
                #maticak-modal-wrapper .predmet-btn:hover {\
                    background: #0080cc;\
                    color: white;\
                    transform: translateY(-2px);\
                }\
                #maticak-modal-wrapper .predmety-container {\
                    display: flex;\
                    flex-wrap: wrap;\
                    gap: 5px;\
                    margin-top: 10px;\
                }\
                #maticak-modal-wrapper .modal-body strong {\
                    color: #1D1D1F;\
                }\
                #maticak-modal-wrapper table {\
                    width: 100%;\
                    border-collapse: collapse;\
                    font-size: 13px;\
                    margin-top: 10px;\
                }\
                #maticak-modal-wrapper table th,\
                #maticak-modal-wrapper table td {\
                    border: 1px solid #ddd;\
                    padding: 6px 8px;\
                    text-align: left;\
                }\
                #maticak-modal-wrapper table th {\
                    background: #006aac;\
                    color: white;\
                    font-weight: 600;\
                }\
                #maticak-modal-wrapper table tr:nth-child(even) {\
                    background: #f5f7fa;\
                }\
                #maticak-modal-wrapper .spinner {\
                    border: 3px solid #f3f3f3;\
                    border-top: 3px solid #0080cc;\
                    border-radius: 50%;\
                    width: 20px;\
                    height: 20px;\
                    animation: maticakSpin 1s linear infinite;\
                }\
                @keyframes maticakSpin {\
                    from { transform: rotate(0deg); }\
                    to { transform: rotate(360deg); }\
                }\
                #maticak-modal-wrapper::-webkit-scrollbar {\
                    width: 6px;\
                }\
                #maticak-modal-wrapper::-webkit-scrollbar-thumb {\
                    background: rgba(0, 0, 0, 0.2);\
                    border-radius: 3px;\
                }\
                #maticak-modal-wrapper::-webkit-scrollbar-track {\
                    background: transparent;\
                }\
                @keyframes maticakSlideUp {\
                    from { transform: translateY(60px) scale(0.95); opacity: 0; }\
                    to { transform: translateY(0) scale(1); opacity: 1; }\
                }\
                @media screen and (max-width: 768px) {\
                    #maticak-chatbot-iframe {\
                        bottom: 0;\
                        right: 5%;\
                        left: 5%;\
                        width: 90%;\
                        height: 70vh;\
                        max-height: 600px;\
                        border-radius: 20px 20px 0 0;\
                    }\
                    #maticak-chat-toggle {\
                        top: 5px;\
                        right: 5px;\
                    }\
                    #maticak-chat-toggle img {\
                        width: 100px;\
                    }\
                    #maticak-modal-wrapper {\
                        width: 95%;\
                        max-height: 75vh;\
                    }\
                }\
                @media screen and (max-width: 480px) {\
                    #maticak-chatbot-iframe {\
                        width: 90%;\
                        height: 75vh;\
                        border-radius: 15px 15px 0 0;\
                    }\
                    #maticak-modal-wrapper {\
                        width: 96%;\
                        max-height: 80vh;\
                    }\
                    #maticak-modal-wrapper .modal-content {\
                        padding: 20px;\
                    }\
                    #maticak-modal-wrapper .modal-header h2 {\
                        font-size: 20px;\
                    }\
                    #maticak-modal-wrapper .button-grid {\
                        grid-template-columns: 1fr;\
                    }\
                    #maticak-modal-wrapper .info-link-btn {\
                        padding: 12px 16px;\
                        font-size: 13px;\
                        min-height: 48px;\
                    }\
                }\
            ';
            document.head.appendChild(style);
        },
        
        injectHTML: function() {
            const container = document.createElement('div');
            container.id = 'maticak-chatbot-container';
            container.innerHTML = '<iframe id="maticak-chatbot-iframe" src="' + this.config.chatbotUrl + '" allow="clipboard-write"></iframe><button id="maticak-chat-toggle" title="Otev\u0159\u00edt chat s Mat\u00fdskem"><img src="https://tmutina79-png.github.io/chatbot-rag-ready/Obr%C3%A1zky/MATY_1.png" alt="MATY" draggable="false" /></button>';
            document.body.appendChild(container);
        },
        
        initEventListeners: function() {
            const self = this;
            const toggleBtn = document.getElementById('maticak-chat-toggle');
            const iframe = document.getElementById('maticak-chatbot-iframe');
            
            toggleBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('🖱️ MATY kliknut, isOpen:', self.isOpen);
                self.toggle();
            });
            
            iframe.addEventListener('load', function() {
                self.iframeLoaded = true;
                console.log('✅ MATIČÁK iframe načten');
            });
            
            window.addEventListener('message', function(event) {
                if (!event.data || !event.data.type) return;
                
                if (event.data.type === 'maticak-close') {
                    self.close();
                }
                
                if (event.data.type === 'maticak-modal-open' && event.data.html) {
                    clearTimeout(self.modalCloseTimeout);
                    self.showModal(event.data.html, event.data.scrollToId);
                }
                
                if (event.data.type === 'maticak-modal-update' && event.data.html) {
                    self.updateModal(event.data.html);
                }
                
                if (event.data.type === 'maticak-modal-close') {
                    clearTimeout(self.modalCloseTimeout);
                    self.modalCloseTimeout = setTimeout(function() {
                        self.removeModal();
                    }, 50);
                }
            });
        },
        
        showModal: function(html, scrollToId) {
            this.removeModal();
            
            var processedHtml = html.replace(/onclick="([^"]*)"/g, 'data-iframe-action="$1"');
            
            var overlay = document.createElement('div');
            overlay.id = 'maticak-modal-overlay';
            
            var wrapper = document.createElement('div');
            wrapper.id = 'maticak-modal-wrapper';
            wrapper.innerHTML = processedHtml;
            
            overlay.appendChild(wrapper);
            document.body.appendChild(overlay);
            
            // Scroll na konkrétní sekci, pokud je zadaná
            if (scrollToId) {
                setTimeout(function() {
                    var target = wrapper.querySelector('#' + scrollToId);
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        target.style.transition = 'background-color 0.3s';
                        target.style.backgroundColor = '#e6f3ff';
                        setTimeout(function() { target.style.backgroundColor = ''; }, 1500);
                    }
                }, 150);
            }
            
            var self = this;
            overlay.addEventListener('click', function(e) {
                if (e.target === overlay) {
                    self.closeModalAndNotify();
                }
            });
            
            this.addModalClickHandlers(wrapper);
        },
        
        updateModal: function(html) {
            var wrapper = document.getElementById('maticak-modal-wrapper');
            if (wrapper) {
                var processedHtml = html.replace(/onclick="([^"]*)"/g, 'data-iframe-action="$1"');
                wrapper.innerHTML = processedHtml;
            }
        },
        
        addModalClickHandlers: function(wrapper) {
            var self = this;
            wrapper.addEventListener('click', function(e) {
                var target = e.target.closest('[data-iframe-action]');
                if (target) {
                    e.preventDefault();
                    e.stopPropagation();
                    var action = target.getAttribute('data-iframe-action');
                    
                    if (action.indexOf('close') !== -1 || action.indexOf('Close') !== -1) {
                        self.removeModal();
                    }
                    
                    var iframe = document.getElementById('maticak-chatbot-iframe');
                    if (iframe && iframe.contentWindow) {
                        iframe.contentWindow.postMessage({
                            type: 'maticak-action',
                            action: action
                        }, '*');
                    }
                }
            });
        },
        
        closeModalAndNotify: function() {
            this.removeModal();
            var iframe = document.getElementById('maticak-chatbot-iframe');
            if (iframe && iframe.contentWindow) {
                iframe.contentWindow.postMessage({
                    type: 'maticak-action',
                    action: 'notifyModalClose()'
                }, '*');
            }
        },
        
        removeModal: function() {
            var overlay = document.getElementById('maticak-modal-overlay');
            if (overlay) overlay.remove();
        },
        
        showGreeting: function() {
            var self = this;
            setTimeout(function() {
                if (self.isOpen) return;
                var toggleBtn = document.getElementById('maticak-chat-toggle');
                var bubble = document.createElement('div');
                bubble.id = 'maticak-greeting-bubble';
                bubble.textContent = 'Ahoj! \uD83D\uDC4B Jmenuji se MATY!';
                if (toggleBtn) toggleBtn.classList.add('maticak-pulse');
                bubble.addEventListener('click', function() {
                    bubble.remove();
                    if (toggleBtn) toggleBtn.classList.remove('maticak-pulse');
                    self.open();
                });
                document.body.appendChild(bubble);
                setTimeout(function() {
                    if (bubble.parentNode) {
                        bubble.classList.add('maticak-bubble-out');
                        setTimeout(function() { bubble.remove(); }, 300);
                    }
                    if (toggleBtn) toggleBtn.classList.remove('maticak-pulse');
                }, 8000);
            }, 1500);
        },

        toggle: function() {
            var iframe = document.getElementById('maticak-chatbot-iframe');
            var btn = document.getElementById('maticak-chat-toggle');
            
            this.isOpen = !this.isOpen;
            
            if (this.isOpen) {
                iframe.classList.add('maticak-visible');
                btn.style.opacity = '0';
                btn.style.pointerEvents = 'none';
                btn.style.transform = 'scale(0.5)';
            } else {
                iframe.classList.remove('maticak-visible');
                btn.style.opacity = '1';
                btn.style.pointerEvents = 'auto';
                btn.style.transform = '';
            }
        },
        
        open: function() {
            if (!this.isOpen) {
                this.toggle();
            }
        },
        
        close: function() {
            if (this.isOpen) {
                this.toggle();
            }
        }
    };
    
    window.MaticakChatbot = MaticakChatbot;
    
})(window);
