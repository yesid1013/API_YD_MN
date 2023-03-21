from utils.db import db
from models import *
from models import Productos

class Stock_detalles (db.Model):
    __tablename__ = 'stock_detalles'
    id_stock_det = db.Column(db.Integer, primary_key = True)
    id_stock_enc = db.Column(db.Integer, db.ForeignKey('stock_encabezado.id_stock_enc'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    def __init__(self,id_stock_enc,id_producto,cantidad) :
        self.id_stock_enc = id_stock_enc
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.estado = 1
    
    def getDatos(self):
        return {
            "id_stock_det": self.id_stock_det,
            "id_stock_enc" : self.id_stock_enc,
            "id_producto" : self.id_producto,
            "cantidad" : self.cantidad,
            "estado" : self.estado
        }
        





