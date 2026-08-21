import sqlite3
import json
from utils import load_data

data = load_data("notes.json")

with sqlite3.connect("data.db") as connection:
    cursor = connection.cursor()

    # SOLUÇÃO: Garante que a tabela 'notes' exista antes de inserir os dados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            details TEXT NOT NULL
        )
    ''')

    for nota in data:
        title = nota['titulo']
        details = nota['detalhes']

        cursor.execute(
            "INSERT INTO notes (title, details) VALUES (?,?)",
            (title, details)
        )
        print(f"Inserido com sucesso: {title}")

    # Salva a criação da tabela e todas as inserções de uma vez só
    connection.commit()

print("\nProcesso finalizado! Todos os itens foram salvos no banco.")
