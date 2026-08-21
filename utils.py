import json 

def load_data (nome_arquivo):
    with open(f'static/data/{nome_arquivo}', 'r') as texto:
        return json.load(texto)

def load_template (template_name):
    with open(f'static/templates/{template_name}', 'r') as arquivo:
        return arquivo.read()

def append_data (params):
    data = load_data("notes.json")

    new_data = {
        'titulo': params['titulo'],
        'detalhes': params['detalhes']
    }

    data.append(new_data)

    with open ('static/data/notes.json', 'w') as f:
        json.dump(data, indent=4, fp=f)

    return data