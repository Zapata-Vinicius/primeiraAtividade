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

        cursor.execute("SELECT id, title, content FROM note")
        dados_do_banco = cursor.fetchall()

    notes_li = [
        note_template.format(id=note[0], title=note[1], content=note[2])
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

def edit (id):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, title, content FROM note WHERE id = ?",
            (id, )
        )   

        note = cursor.fetchone()

        if note:
            return load_template("update.html").format(
                id=note[0],
                title=note[1],
                content=note[2]
            )

        return "Nota não encontrada", 404

def update (id, titulo, detalhes):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE note SET title = ?, content = ? WHERE id = ?",
            (titulo,detalhes,id)
        )   
        connection.commit()