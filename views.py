from utils import load_data, load_template, append_data
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit (titulo, detalhes):
    params = {
        "titulo":titulo,
        "detalhes":detalhes
    }

    append_data(params)