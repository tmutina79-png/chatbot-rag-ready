"""
Databázový model pro ukládání konverzací
"""
import sqlite3
from datetime import datetime
from typing import List, Dict, Optional
import json

class ConversationDB:
    def __init__(self, db_path: str = "conversations.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Vytvoří databázové tabulky, pokud neexistují"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabulka pro uživatele
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_messages INTEGER DEFAULT 0
            )
        """)
        
        # Tabulka pro zprávy
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                message TEXT NOT NULL,
                response TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def save_conversation(self, user_id: str, message: str, response: str):
        """Uloží konverzaci do databáze"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Uložit nebo aktualizovat uživatele
        cursor.execute("""
            INSERT INTO users (user_id, first_seen, last_seen, total_messages)
            VALUES (?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1)
            ON CONFLICT(user_id) DO UPDATE SET
                last_seen = CURRENT_TIMESTAMP,
                total_messages = total_messages + 1
        """, (user_id,))
        
        # Uložit zprávu
        cursor.execute("""
            INSERT INTO messages (user_id, message, response)
            VALUES (?, ?, ?)
        """, (user_id, message, response))
        
        conn.commit()
        conn.close()
    
    def get_user_history(self, user_id: str, limit: int = 10) -> List[Dict]:
        """Získá historii konverzací uživatele"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT message, response, timestamp
            FROM messages
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        """, (user_id, limit))
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                "message": row[0],
                "response": row[1],
                "timestamp": row[2]
            }
            for row in results
        ]
    
    def get_user_stats(self, user_id: str) -> Optional[Dict]:
        """Získá statistiky uživatele"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT first_seen, last_seen, total_messages
            FROM users
            WHERE user_id = ?
        """, (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                "first_seen": result[0],
                "last_seen": result[1],
                "total_messages": result[2]
            }
        return None
    
    def get_all_conversations(self, limit: int = 50) -> List[Dict]:
        """Získá všechny nedávné konverzace"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT user_id, message, response, timestamp
            FROM messages
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                "user_id": row[0],
                "message": row[1],
                "response": row[2],
                "timestamp": row[3]
            }
            for row in results
        ]
