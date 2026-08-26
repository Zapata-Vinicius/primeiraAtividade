from flask import Flask, render_template_string, request, redirect
import views



app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/update/<int:id>', methods=["POST","GET"])
def edit_note (id):
    if request.method == 'POST':
        titulo = request.form.get("titulo")
        detalhes = request.form.get("detalhes")
        views.update(id, titulo, detalhes)
        return redirect("/")

    return render_template_string(views.edit(id))

if __name__ == '__main__':
    app.run(debug=True)