from flask import render_template

def register_app(app):    
    @app.route("/")
    def inicio():
        titulo = "Mi aplicación web"
        elementos = [
            {},
            {},
            {}]
        return render_template("index.html", titulo = titulo, elementos = elementos)
    