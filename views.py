import sqlite3
from utils import load_template


def index():
    note_template = load_template("components/note.html")

    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """
        )

        cursor.execute("SELECT title, content FROM note")
        dados_do_banco = cursor.fetchall()

    notes_li = [
        note_template.format(title=note[0], content=note[1])
        for note in dados_do_banco
    ]
    notes = "\n".join(notes_li)

    return load_template("index.html").format(notes=notes)


def submit(titulo, detalhes):

    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """
        )

        cursor.execute(
            "INSERT INTO note (title, content) VALUES (?, ?)",
            (titulo, detalhes),
        )
        connection.commit()
