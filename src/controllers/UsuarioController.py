from flask import jsonify, request
from models.Usuario import *
from models.Locales import Locales
from models.Admin_departamentos import Admin_departamentos
from flask_jwt_extended import get_jwt_identity
def agregar_usuario():
    try:
        num_documento = request.json['num_documento']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        email = request.json['email']
        password = request.json['password']
        cargo = request.json['cargo']
        new_user = Usuario(num_documento,nombre,apellido,email,password,cargo)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuario insertado", "status" : 200})
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def cargar_dashboard():
    try:
        current_user_id = get_jwt_identity() #Obtengo el id del usuario que ingreso
        user = Usuario.query.get(current_user_id) #En la variable user obtengo el usuario que ingreso

        if user.cargo == 1: #verifico el cargo 
            id_local= db.session.query(Locales.id_local).filter(Locales.id_user==user.id_user).first() #consulta
            return jsonify(id_local)

        if user.cargo == 2:
            id_departamento = db.session.query(Admin_departamentos.id_departamento).filter(Admin_departamentos.id_user == user.id_user).first()
            return jsonify(id_departamento)
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()


