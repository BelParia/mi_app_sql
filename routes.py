from flask import render_template, request, redirect, url_for
from models import Contacto
from extensions import db

def register_app(app):    
    @app.route("/")
    def inicio():
        contactos = Contacto.query.all()
        return render_template("index.html", contactos=contactos)

    @app.route("/crear", methods = ['GET'])  ## metodo de tipo GET (conseguir datos)
    def ver_creacion_contacto():
        return render_template('crear.html')

    @app.route("/crear", methods = ['POST'])  ## metodo de tipo POST (enviar datos)
    def crear():
        ## formar el contacto, el nuevo objeto
        nuevo_contacto= Contacto(
            nombre = request.form['nombre'],
            telefono = request.form['telefono'],
            email = request.form['email']
        )
        ## guardar el nuevo_contacto en la base de datos
        db.session.add(nuevo_contacto)
        db.session.commit()
        return redirect(url_for('inicio'))  ## redirigiendo al inicio, listado de contactos  

    @app.route("/editar")
    def editar():
        return render_template("editar.html")

    @app.route("/eliminar", methods=["GET", "POST"])
    def eliminar():
        if request.method == "POST":
            # TODO: eliminar el contacto de la base de datos
            return redirect(url_for("inicio"))
        return render_template("eliminar.html")    