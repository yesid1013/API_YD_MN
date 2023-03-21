from utils.db import db
from models import Locales
from models.Admin_departamentos import Admin_departamentos

class Departamentos(db.Model):
    __tablename__ = 'departamentos'
    id_departamento = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.Integer, nullable = False, default = 1)
    
    locales = db.relationship('Locales', backref='departamentos', lazy=True)
    admin_departamentos = db.relationship('Admin_departamentos', backref = 'departamentos')

    def __init__(self,nombre) :
        self.nombre = nombre
        self.estado = 1

    def getDatos(self):
        return {
            "id_departamento" : self.id_departamento,
            "nombre" : self.nombre,
            "estado" : self.estado
        }

        
