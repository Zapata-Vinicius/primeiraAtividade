import sqlite3
from utils import load_template


def index():
    note_template = load_template("components/note.html")

    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, content FROM notes")
        dados_do_banco = cursor.fetchall() 


    notes_li = [
        note_template.format(title=note[1], content=note[2])
        for note in dados_do_banco
    ]
    notes = "\n".join(notes_li)

    return load_template("index.html").format(notes=notes)


def submit(titulo, detalhes):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (?, ?)",
            (titulo, detalhes),
        )
        connection.commit()
