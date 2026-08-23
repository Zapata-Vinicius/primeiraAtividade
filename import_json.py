import sqlite3
from utils import load_data

data = load_data("notes.json")

with sqlite3.connect("banco.db") as connection:
    cursor = connection.cursor()

    # Cria a tabela sem restrição UNIQUE (permite títulos iguais)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """
    )

    # Limpa dados antigos de testes para não duplicar antes de importar o JSON oficial
    cursor.execute("DELETE FROM notes")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='notes'")

    # Insere tudo do JSON para o Banco
    for nota in data:
        title = nota["titulo"]
        content = nota["detalhes"]
        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?,?)", (title, content)
        )

    connection.commit()
print("Migração concluída com sucesso!")
