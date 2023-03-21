from flask import jsonify, request
from models.Usuario import *
from flask_jwt_extended import create_access_token, set_access_cookies,unset_jwt_cookies


def login():
    try:
        username = request.json["usuario"]
        password = request.json["contraseña"]

        usuario = Usuario.query.filter_by(email=username).first()
        if not usuario:
            return jsonify({"message" : "Usuario no encontrado" , "status" : 404}) , 404
        else:
            if usuario.password != password:
                return jsonify({
                    'message': 'contraseña incorrecta',
                    'status': '400'
                    }) , 400
        
            else:
                access_token = create_access_token(identity=usuario.id_user)                
                return jsonify(token=access_token)

    except Exception as e:
        return jsonify({"Ha ocurrido un error " : str(e) })
    
def logout():
    try:
        resp = jsonify({'logout': "ok"})
        unset_jwt_cookies(resp)
        return resp

    except Exception as e:
        return jsonify({"Ha ocurrido un error " : str(e) })