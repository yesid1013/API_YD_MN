from utils.db import db
from models import *

class Parametros_detalles (db.Model):
    __tablename__ = 'parametros_detalles'
    id_dparam = db.Column(db.Integer, primary_key = True)
    id_param = db.Column(db.Integer, db.ForeignKey('parametros_encabezado.id_param'), nullable=False)
    nombre = db.Column(db.String(30),nullable = False)
    abreviado = db.Column(db.String(50),nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    def __init__(self,id_param,nombre,abreviado):
        self.id_param = id_param
        self.nombre = nombre
        self.abreviado = abreviado
        self.estado = 1

    def getDatos(self):
        return {
            "id_dparam" : self.id_dparam,
            "id_param" : self.id_param,
            "nombre" : self.nombre,
            "abreviado" : self.abreviado,
            "estado" : self.estado
        } 
        