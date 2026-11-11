import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("DB_HOST", "localhost")
PORTA = int(os.getenv("DB_PORT", "5432"))
USUARIO = os.getenv("DB_USER", "postgres")
SENHA = os.getenv("DB_PASSWORD", "")
NOME_BANCO = os.getenv("DB_NAME", "escola")

def conectar():
    return psycopg2.connect(
        host = HOST, port = PORTA, dbname = NOME_BANCO, user = USUARIO, password = SENHA
    )
    
def criar_banco():
    conexao = psycopg2.connect(
        host = HOST, port = PORTA, dbname = "postgres", user = USUARIO, password = SENHA
    )
    
    conexao.autocommit = True
    cursor = conexao.cursor()
    
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (NOME_BANCO,))
    if cursor.fetchone() is None:
        cursor.execute(f"CREATE DATABASE {NOME_BANCO}")
        
    conexao.close()
    
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota REAL NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
    
if __name__ == "__main__":
    criar_banco()
    criar_tabela()
    print("Conectou! Banco e tabela prontos.")
    
    