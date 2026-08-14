from flask import Flask
from extensions import db
from models import Contacto
from routes import register_app

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

def cargar_datos_iniciales():
    contactos = [
        Contacto(nombre="Ana García", telefono="918730095", email="anagar@gmail.com"),
        Contacto(nombre="Luis Fernández", telefono="987123456", email="luis.fernandez@gmail.com"),
        Contacto(nombre="María Torres", telefono="976543210", email="maria.torres@gmail.com"),
        Contacto(nombre="Carlos Ramírez", telefono="965432109", email="carlos.ramirez@gmail.com"),
        Contacto(nombre="Lucía Mendoza", telefono="954321098", email="lucia.mendoza@gmail.com"),
        Contacto(nombre="Pedro Salazar", telefono="943210987", email="pedro.salazar@gmail.com"),
        Contacto(nombre="Rosa Castillo", telefono="932109876", email="rosa.castillo@gmail.com"),
        Contacto(nombre="Jorge Rojas", telefono="921098765", email="jorge.rojas@gmail.com"),
        Contacto(nombre="Camila Vargas", telefono="910987654", email="camila.vargas@gmail.com"),
        Contacto(nombre="Diego Aguilar", telefono="909876543", email="diego.aguilar@gmail.com"),
    ]
    if Contacto.query.count() == 0:
        db.session.add_all(contactos)
        db.session.commit()

register_app(app=app)

## ejecutar el programa
## solo en este archivo
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_datos_iniciales()
    app.run(debug=True)
