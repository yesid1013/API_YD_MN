from utils.db import db
from models import Stock_detalles

class Stock_encabezado (db.Model):
    __tablename__ = 'stock_encabezado'
    id_stock_enc = db.Column(db.Integer, primary_key = True)
    id_local = db.Column(db.Integer, db.ForeignKey('locales.id_local'), nullable=False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    stock_detalles = db.relationship('Stock_detalles', backref='stock_encabezado', lazy=True)


    def __init__(self,id_local) :
        self.id_local = id_local
        self.estado = 1

    def getDatos(self):
        return {
            "id_stock_enc" : self.id_stock_enc,
            "id_local" : self.id_local,
            "estado" : self.estado
        }



