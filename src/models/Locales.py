from utils.db import db
from models import Stock_encabezado,Factura_encabezado

class Locales (db.Model):
    __tablename__ = 'locales'
    id_local = db.Column(db.Integer, primary_key = True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamentos.id_departamento'), nullable=False)
    nombre = db.Column(db.String(20),nullable = False)
    direccion = db.Column(db.String(50),nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('usuarios.id_user'), nullable=False)
    estado = db.Column(db.Integer, nullable = False, default = 1)
    
    stock_encabezado = db.relationship('Stock_encabezado', backref='locales', lazy=True)
    factura_encabezado = db.relationship('Factura_encabezado', backref='locales', lazy=True)



    def __init__(self,id_departamento,nombre,direccion,id_user):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.direccion = direccion
        self.id_user = id_user
        self.estado = 1

    def getDatos(self):
        return {
            "id_local" : self.id_local,
            "id_departamento" : self.id_departamento,
            "nombre" : self.nombre,
            "direccion" : self.direccion,
            "id_user" : self.id_user,
            "estado" : self.estado
        }




