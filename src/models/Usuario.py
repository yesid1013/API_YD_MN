from utils.db import db
from models.Locales import Locales
from models.Admin_departamentos import Admin_departamentos
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_user = db.Column(db.Integer, primary_key = True)
    num_documento = db.Column(db.String(20), unique=True, nullable = False)
    nombre = db.Column(db.String(20),nullable = False)
    apellido = db.Column(db.String(20),nullable = False)
    email = db.Column(db.String(20), unique= True, nullable = False)
    password = db.Column(db.String(20), nullable = False)
    cargo = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.Integer, nullable = False, default = 1)
    
    locales = db.relationship('Locales', backref='usuarios', lazy=True)
    admin_departamentos = db.relationship('Admin_departamentos', backref='usuarios', lazy=True)


    def __init__(self,num_documento,nombre,apellido,email,password,cargo) :
        self.num_documento = num_documento
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.cargo = cargo
        self.estado = 1

    def getDatos(self):
        return {
            "id_user" : self.id_user,
            "documento" : self.num_documento,
            "nombre" : self.nombre,
            "apellido" : self.apellido,
            "email" : self.email,
            "password" : self.password,
            "cargo" : self.cargo,
            "estado" : self.estado
        }

    
