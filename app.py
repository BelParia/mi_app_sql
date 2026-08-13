from flask import Flask
from routes import register_app

app = Flask(__name__)

register_app(app=app)  # la segunda app es en sì la app de arriba DX

## ejecutar el programa
## solo en este archivo
if __name__ == '__main__':
    app.run(debug=True)