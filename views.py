import sqlite3
from utils import load_template, get_note_by_id


def index():
    note_template = load_template("components/note.html")

    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, title, content, is_favorite FROM note ORDER BY is_favorite DESC, id DESC"
        )
        dados_do_banco = cursor.fetchall()

    notes_li = []
    for note in dados_do_banco:
        is_fav = note[3]
        favorite_class = "favorite-card" if is_fav else ""
        favorite_icon = "★" if is_fav else "☆"

        formatted_note = note_template.format(
            id=note[0],
            title=note[1],
            content=note[2],
            favorite_class=favorite_class,
            favorite_icon=favorite_icon
        )
        notes_li.append(formatted_note)

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
                content TEXT NOT NULL,
                is_favorite INTEGER DEFAULT 0
            )
        """
        )
        cursor.execute(
            "INSERT INTO note (title, content, is_favorite) VALUES (?, ?, 0)",
            (titulo, detalhes),
        )
        connection.commit()


def delete(id):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM note WHERE id = ?", (id,))
        connection.commit()


def edit(id):
    note = get_note_by_id(id)

    if note:
        return load_template("update.html").format(
            id=note["id"], title=note["title"], content=note["content"]
        )

    return "Nota não encontrada", 404


def update(id, titulo, detalhes):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE note SET title = ?, content = ? WHERE id = ?",
            (titulo, detalhes, id),
        )
        connection.commit()


def favorite(id):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE note SET is_favorite = NOT is_favorite WHERE id = ?",
            (id,),
        )
        connection.commit()