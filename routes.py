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

    @app.route("/editar/<int:id>", methods=["GET", "POST"])
    def editar(id):
        contacto = Contacto.query.get_or_404(id)
        if request.method == "POST":
            contacto.nombre = request.form['nombre']
            contacto.telefono = request.form['telefono']
            contacto.email = request.form['email']
            db.session.commit()
            return redirect(url_for('inicio'))
        return render_template("editar.html", contacto=contacto)

    @app.route("/eliminar/<int:id>", methods=["GET", "POST"])
    def eliminar(id):
        contacto = Contacto.query.get_or_404(id)
        if request.method == "POST":
            db.session.delete(contacto)
            db.session.commit()
            return redirect(url_for("inicio"))
        return render_template("eliminar.html", contacto=contacto)