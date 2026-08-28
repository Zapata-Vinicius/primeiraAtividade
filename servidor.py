import sqlite3
from flask import Flask, render_template_string, request, redirect
import views

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
    connection.commit()

app = Flask(__name__)
app.static_folder = "static"


@app.route("/")
def index():
    return render_template_string(views.index())


@app.route("/submit", methods=["POST"])
def submit_form():
    titulo = request.form.get("titulo")
    detalhes = request.form.get("detalhes")

    views.submit(titulo, detalhes)
    return redirect("/")


@app.route("/update/<int:id>", methods=["GET"])
def edit_note(id):
    return render_template_string(views.edit(id))


@app.route("/update", methods=["POST"])
def update_note():
    id = request.form.get("id")
    titulo = request.form.get("titulo")
    detalhes = request.form.get("detalhes")

    views.update(id, titulo, detalhes)
    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete_noteid(id):
    views.delete(id)
    return redirect("/")


@app.route("/favorite/<int:id>", methods=["POST", "GET"])
def favorite_note(id):
    views.favorite(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)