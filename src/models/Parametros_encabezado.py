from utils.db import db
from models import Parametros_detalles

class Parametros_encabezado(db.Model):
    __tablename__ = 'parametros_encabezado'
    id_param = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20), nullable = False)
    abreviado = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)
    
    parametros_detalles = db.relationship('Parametros_detalles', backref='parametros_enc', lazy=True)


    def __init__(self,nombre,abreviado) :
        self.nombre = nombre
        self.abreviado = abreviado
        self.estado = 1

    def getDatos(self):
        return {
            "id_param" : self.id_param,
            "nombre" : self.nombre,
            "abreviado" : self.abreviado,
            "estado" : self.estado
        }

