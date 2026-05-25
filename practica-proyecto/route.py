from flask import Blueprint, render_template
mis_rutas = Blueprint("nombre-1", __name__)

@mis_rutas.route("/libreria")
def inicio():
    return render_template("libros.html")
@mis_rutas.route("/libreria/<int:id>")
def libro(id):
    if id == 1:
        return render_template("libro-blanca-nieves.html")
    elif id == 2:
        return render_template("libro-caperucita-roja.html")
    else:
        return "LIBRO no encontrado"