import json 

def load_template (template_name):
    with open(f'static/templates/{template_name}', 'r') as arquivo:
        return arquivo.read()