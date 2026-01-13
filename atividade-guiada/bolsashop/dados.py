import sqlite3
import os

DB_NAME = "ecommerce_db"

def criar_banco():
    
    #if os.path.exist(DB_NAME):
    #    os.remove(DB_NAME)
    
    # conexão DB:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 1. Habilitar Chaves Estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_nome TEXT,
        valor_bruto REAL NOT NULL,
        status TEXT DEFAULT 'PENDENTE'
    );                            
    """)
    
    cursor.execute("""
    CREATE TABLE pagamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        metodo TEXT,
        valor_final REAL,
        pedido_id INTEGER,
        FOREIGN KEY (pedido_id) REFERENCES pedidos(id)  
    );
    """)
    
    pedidos = [
        ("João", 1000.00),
        ("Maria", 500.00),
        ("Carlos", 2000.00)
    ]
    
    cursor.executemany(
        "INSERT INTO pedidos (cliente_nome, valor_bruto) VALUES (?, ?)",
        pedidos
    )
    
    conn.commit()
    print("Banco de Dados gerado!")
    conn.close()

if __name__ == "__main__":
    criar_banco()