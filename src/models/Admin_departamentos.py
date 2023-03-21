from utils.db import db

class Admin_departamentos (db.Model):
    __tablename__ = 'admin_departamentos'
    id_admin_dep = db.Column(db.Integer, primary_key = True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamentos.id_departamento'), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('usuarios.id_user'), nullable=False)
    estado = db.Column(db.Integer, nullable = False, default = 1)

    def __init__(self,id_departamento,id_user) :
        self.id_departamento = id_departamento
        self.id_user = id_user
        self.estado = 1
