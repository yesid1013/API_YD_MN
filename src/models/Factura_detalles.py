from utils.db import db
from models import *

class Factura_detalles(db.Model):
    __tablename__ = 'factura_detalles'
    id_fac_det = db.Column(db.Integer, primary_key = True)
    id_fac_enc = db.Column(db.Integer, db.ForeignKey('factura_encabezado.id_fac_enc'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    precio = db.Column(db.Integer, nullable = False)
    cantidad = db.Column(db.Integer, nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    def __init__(self,id_fac_enc,id_producto,precio,cantidad) :
        self.id_fac_enc = id_fac_enc
        self.id_producto = id_producto
        self.precio = precio
        self.cantidad = cantidad
        self.estado = 1
    
    def getDatos(self):
        return {
            "id_fac_det": self.id_fac_det,
            "id_fac_enc" : self.id_fac_enc,
            "id_producto" : self.id_producto,
            "precio" : self.precio,
            "cantidad" : self.cantidad,
            "estado" : self.estado
        }

