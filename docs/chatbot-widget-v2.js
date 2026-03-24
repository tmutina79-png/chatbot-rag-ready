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
                    bottom: ' + this.config.position.bottom + ';\
                    right: ' + this.config.position.right + ';\
                    width: 64px;\
                    height: 64px;\
                    background: linear-gradient(135deg, #006aac 0%, #0a78b0 100%);\
                    color: white;\
                    border: none;\
                    border-radius: 50%;\
                    font-size: 30px;\
                    cursor: pointer;\
                    box-shadow: 0 8px 24px rgba(0, 106, 172, 0.35);\
                    z-index: 999998;\
                    transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);\
                    border: 2px solid rgba(255, 255, 255, 0.2);\
                    display: flex;\
                    align-items: center;\
                    justify-content: center;\
                }\
                #maticak-chat-toggle:hover {\
                    transform: scale(1.08) translateY(-2px);\
                    box-shadow: 0 12px 32px rgba(0, 106, 172, 0.45);\
                }\
                #maticak-chat-toggle:active {\
                    transform: scale(0.96);\
                }\
                #maticak-chat-toggle.maticak-hidden {\
                    display: none;\
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
                        width: 60px;\
                        height: 60px;\
                        font-size: 28px;\
                        bottom: 15px;\
                        right: 15px;\
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
                }\
            ';
            document.head.appendChild(style);
        },
        
        injectHTML: function() {
            const container = document.createElement('div');
            container.id = 'maticak-chatbot-container';
            container.innerHTML = '<iframe id="maticak-chatbot-iframe" src="' + this.config.chatbotUrl + '" allow="clipboard-write"></iframe><button id="maticak-chat-toggle">💬</button>';
            document.body.appendChild(container);
        },
        
        initEventListeners: function() {
            const self = this;
            const toggleBtn = document.getElementById('maticak-chat-toggle');
            const iframe = document.getElementById('maticak-chatbot-iframe');
            
            toggleBtn.addEventListener('click', function() {
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
                    self.showModal(event.data.html);
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
        
        showModal: function(html) {
            this.removeModal();
            
            var processedHtml = html.replace(/onclick="([^"]*)"/g, 'data-iframe-action="$1"');
            
            var overlay = document.createElement('div');
            overlay.id = 'maticak-modal-overlay';
            
            var wrapper = document.createElement('div');
            wrapper.id = 'maticak-modal-wrapper';
            wrapper.innerHTML = processedHtml;
            
            overlay.appendChild(wrapper);
            document.body.appendChild(overlay);
            
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
                this.addModalClickHandlers(wrapper);
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
        
        toggle: function() {
            var iframe = document.getElementById('maticak-chatbot-iframe');
            var btn = document.getElementById('maticak-chat-toggle');
            
            this.isOpen = !this.isOpen;
            
            if (this.isOpen) {
                iframe.classList.add('maticak-visible');
                btn.classList.add('maticak-hidden');
            } else {
                iframe.classList.remove('maticak-visible');
                btn.classList.remove('maticak-hidden');
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
