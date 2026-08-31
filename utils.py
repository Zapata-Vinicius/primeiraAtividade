import sqlite3


def load_template(template_name):
    with open(f"static/templates/{template_name}", "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def get_note_by_id(note_id):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, title, content, is_favorite FROM note WHERE id = ?", (note_id,)
        )
        row = cursor.fetchone()

        if row:
            return {
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "is_favorite": row[3],
            }
    return None