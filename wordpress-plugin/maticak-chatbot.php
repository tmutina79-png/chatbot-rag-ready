<?php
/**
 * Plugin Name: MATIČÁK Chatbot
 * Plugin URI: https://mgo.cz
 * Description: AI chatbot pomocník pro Matiční gymnázium Ostrava
 * Version: 1.0.0
 * Author: Žáci MGO
 * Author URI: https://mgo.cz
 * License: GPL v2 or later
 * Text Domain: maticak-chatbot
 */

// Zabránění přímému přístupu
if (!defined('ABSPATH')) {
    exit;
}

// Definice konstant
define('MATICAK_CHATBOT_VERSION', '1.0.0');
define('MATICAK_CHATBOT_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('MATICAK_CHATBOT_PLUGIN_URL', plugin_dir_url(__FILE__));

/**
 * Třída pro MATIČÁK Chatbot
 */
class Maticak_Chatbot {
    
    /**
     * Konstruktor
     */
    public function __construct() {
        // Aktivace pluginu
        register_activation_hook(__FILE__, array($this, 'activate'));
        
        // Deaktivace pluginu
        register_deactivation_hook(__FILE__, array($this, 'deactivate'));
        
        // Přidání admin menu
        add_action('admin_menu', array($this, 'add_admin_menu'));
        
        // Registrace nastavení
        add_action('admin_init', array($this, 'register_settings'));
        
        // Přidání chatbot scriptu do frontendu
        add_action('wp_footer', array($this, 'add_chatbot_widget'));
    }
    
    /**
     * Aktivace pluginu
     */
    public function activate() {
        // Nastavení výchozích hodnot
        add_option('maticak_chatbot_api_url', 'http://127.0.0.1:8000');
        add_option('maticak_chatbot_enabled', '1');
    }
    
    /**
     * Deaktivace pluginu
     */
    public function deactivate() {
        // Volitelně: vymazat nastavení
        // delete_option('maticak_chatbot_api_url');
        // delete_option('maticak_chatbot_enabled');
    }
    
    /**
     * Přidání admin menu
     */
    public function add_admin_menu() {
        add_options_page(
            'MATIČÁK Chatbot Nastavení',
            'MATIČÁK Chatbot',
            'manage_options',
            'maticak-chatbot',
            array($this, 'settings_page')
        );
    }
    
    /**
     * Registrace nastavení
     */
    public function register_settings() {
        register_setting('maticak_chatbot_settings', 'maticak_chatbot_api_url');
        register_setting('maticak_chatbot_settings', 'maticak_chatbot_enabled');
    }
    
    /**
     * Stránka s nastavením
     */
    public function settings_page() {
        ?>
        <div class="wrap">
            <h1>🤖 MATIČÁK Chatbot - Nastavení</h1>
            
            <form method="post" action="options.php">
                <?php settings_fields('maticak_chatbot_settings'); ?>
                <?php do_settings_sections('maticak_chatbot_settings'); ?>
                
                <table class="form-table">
                    <tr valign="top">
                        <th scope="row">Povolit chatbot</th>
                        <td>
                            <label>
                                <input type="checkbox" 
                                       name="maticak_chatbot_enabled" 
                                       value="1" 
                                       <?php checked(get_option('maticak_chatbot_enabled'), '1'); ?> />
                                Zobrazit chatbot na webu
                            </label>
                        </td>
                    </tr>
                    
                    <tr valign="top">
                        <th scope="row">API URL</th>
                        <td>
                            <input type="text" 
                                   name="maticak_chatbot_api_url" 
                                   value="<?php echo esc_attr(get_option('maticak_chatbot_api_url')); ?>" 
                                   class="regular-text" 
                                   placeholder="http://127.0.0.1:8000" />
                            <p class="description">
                                URL adresa tvého FastAPI backend serveru (např. http://TVOJE-IP:8000)
                            </p>
                        </td>
                    </tr>
                </table>
                
                <?php submit_button(); ?>
            </form>
            
            <hr>
            
            <h2>📋 Instrukce pro instalaci</h2>
            <ol>
                <li>Nahraj soubor <code>chatbot-widget.js</code> do složky <code>/wp-content/uploads/maticak-chatbot/</code></li>
                <li>Nahraj soubor <code>logo_mgo.jpeg</code> do stejné složky</li>
                <li>Nastav API URL výše (IP adresa serveru, kde běží FastAPI)</li>
                <li>Aktivuj chatbot zaškrtnutím políčka výše</li>
                <li>Spusť backend server: <code>python3 -m uvicorn main:app --host 0.0.0.0 --port 8000</code></li>
            </ol>
            
            <h2>🧪 Test připojení</h2>
            <p>
                <button type="button" class="button button-secondary" onclick="testMaticakConnection()">
                    Otestovat připojení k API
                </button>
                <span id="maticak-test-result"></span>
            </p>
            
            <script>
                async function testMaticakConnection() {
                    const apiUrl = '<?php echo esc_js(get_option('maticak_chatbot_api_url')); ?>';
                    const resultEl = document.getElementById('maticak-test-result');
                    
                    resultEl.innerHTML = '⏳ Testuji připojení...';
                    
                    try {
                        const response = await fetch(apiUrl + '/jidelna/dnesni-menu');
                        const data = await response.json();
                        
                        if (data.success) {
                            resultEl.innerHTML = '<span style="color: green;">✅ Připojení úspěšné!</span>';
                        } else {
                            resultEl.innerHTML = '<span style="color: orange;">⚠️ API odpovídá, ale vrací chybu</span>';
                        }
                    } catch (error) {
                        resultEl.innerHTML = '<span style="color: red;">❌ Chyba připojení: ' + error.message + '</span>';
                    }
                }
            </script>
        </div>
        <?php
    }
    
    /**
     * Přidání chatbot widgetu do footeru
     */
    public function add_chatbot_widget() {
        // Kontrola, zda je chatbot povolen
        if (get_option('maticak_chatbot_enabled') !== '1') {
            return;
        }
        
        $api_url = get_option('maticak_chatbot_api_url');
        $widget_url = content_url('/uploads/maticak-chatbot/chatbot-widget.js');
        $logo_url = content_url('/uploads/maticak-chatbot/logo_mgo.jpeg');
        
        ?>
        <!-- MATIČÁK Chatbot -->
        <script src="<?php echo esc_url($widget_url); ?>"></script>
        <script>
            if (typeof MaticakChatbot !== 'undefined') {
                MaticakChatbot.init({
                    apiUrl: '<?php echo esc_js($api_url); ?>',
                    logoPath: '<?php echo esc_js($logo_url); ?>'
                });
            } else {
                console.error('MATIČÁK Chatbot: Widget script nenačten. Nahrajte chatbot-widget.js do /wp-content/uploads/maticak-chatbot/');
            }
        </script>
        <?php
    }
}

// Inicializace pluginu
new Maticak_Chatbot();
