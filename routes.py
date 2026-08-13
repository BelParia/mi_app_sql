from flask import render_template

def register_app(app):    
    @app.route("/")
    def inicio():
        return render_template("index.html")
    