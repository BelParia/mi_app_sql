from flask import render_template, request, redirect, url_for

def register_app(app):    
    @app.route("/")
    def inicio():
        return render_template("index.html")

    @app.route("/crear")
    def crear():
        return render_template("crear.html")

    @app.route("/editar")
    def editar():
        return render_template("editar.html")

    @app.route("/eliminar", methods=["GET", "POST"])
    def eliminar():
        if request.method == "POST":
            # TODO: eliminar el contacto de la base de datos
            return redirect(url_for("inicio"))
        return render_template("eliminar.html")    