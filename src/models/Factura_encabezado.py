from utils.db import db
from models import Factura_detalles

class Factura_encabezado(db.Model):
    __tablename__ = 'factura_encabezado'
    id_fac_enc = db.Column(db.Integer, primary_key = True)
    id_local = db.Column(db.Integer, db.ForeignKey('locales.id_local'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    fecha = db.Column(db.TIMESTAMP)
    precio_total = db.Column(db.Float,nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    factura_detalles = db.relationship('Factura_detalles', backref='factura_encabezado', lazy=True)

    def __init__(self,id_local,id_cliente,precio_total) :
        self.id_local = id_local
        self.id_cliente = id_cliente
        self.precio_total = precio_total
        self.estado = 1

    def getDatos(self):
        return {
            "id_fac_enc" : self.id_fac_enc,
            "id_local" : self.id_local,
            "id_cliente" : self.id_cliente,
            "fecha" : self.fecha,
            "precio_total" : self.precio_total,
            "estado" : self.estado
        }






