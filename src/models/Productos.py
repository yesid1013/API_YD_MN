from utils.db import db
from models import Factura_detalles,Stock_detalles

class Productos(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key = True)
    num_serie = db.Column(db.String(20),nullable = False)
    nombre = db.Column(db.String(20),nullable = False)
    id_tipo_producto = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float,nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    factura_detalles = db.relationship('Factura_detalles', backref='productos', lazy=True)
    stock_detalles = db.relationship('Stock_detalles', backref='productos', lazy=True)

    def __init__(self,num_serie,nombre,id_tipo_producto,precio) :
        self.num_serie = num_serie
        self.nombre = nombre
        self.id_tipo_producto = id_tipo_producto
        self.precio = precio
        self.estado = 1

    def getDatos(self):
        return {
            "id_producto" : self.id_producto,
            "num_serie" : self.num_serie,
            "nombre" : self.nombre,
            "id_tipo_producto" : self.id_tipo_producto,
            "precio" : self.precio,
            "estado" : self.estado
        }

