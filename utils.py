import json 
import sqlite3
from collections import namedtuple

Note = namedtuple("Note", ["id", "title", "content"])

def load_template (template_name):
    with open(f'static/templates/{template_name}', 'r') as arquivo:
        return arquivo.read()

def get_note_by_id(note_id):
    with sqlite3.connect("banco.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                "id": row[0],
                "title": row[1],
                "content": row[2]
            }
    return None