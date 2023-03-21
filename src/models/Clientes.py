from utils.db import db
from models import Factura_encabezado
class Clientes (db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key = True)
    num_documento = db.Column(db.String(11), unique= True, nullable = False)
    nombre = db.Column(db.String(20),nullable = False)
    apellido = db.Column(db.String(20),nullable = False)
    telefono = db.Column(db.String(11),nullable = False)
    email = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    factura_encabezado = db.relationship('Factura_encabezado', backref='clientes', lazy=True)

    def __init__(self,num_documento,nombre,apellido,telefono,email) :
        self.num_documento = num_documento
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.estado = 1

    def getDatos(self):
        return {
            "id_cliente" : self.id_cliente,
            "num_documento" : self.num_documento,
            "nombre": self.nombre,
            "apellido" : self.apellido,
            "telefono" : self.telefono,
            "email" : self.email,
            "estado" : self.estado
        }







