def register_app(app):    
    @app.route("/")
    def inicio():
        return "Hola mundo"