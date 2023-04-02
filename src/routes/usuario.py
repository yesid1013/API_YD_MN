from flask import Blueprint
from controllers import UsuarioController
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin

users = Blueprint('users', __name__)

@cross_origin()
@users.route('/add_user', methods=['POST'])
def usuarios():
    return UsuarioController.agregar_usuario()

@cross_origin()
@users.route('/dashboard', methods = ['GET'])
@jwt_required
def dashboard():
    return UsuarioController.cargar_dashboard()

@cross_origin()
@users.route('/listar_usuarios', methods=['GET'])
def listar_usuarios():
    return UsuarioController.listar_usuarios()

@cross_origin()
@users.route('/listar_usuarios_borrados', methods=['GET'])
def listar_usuarios_borrados():
    return UsuarioController.listar_usuarios_borrados()

@cross_origin()
@users.route('/actualizar_usuario/<id_user>', methods=['PUT'])
def actualizar_usuario(id_user):
    return UsuarioController.editar_usuario(id_user)

@cross_origin()
@users.route('/eliminar_usuario/<id_user>', methods=['DELETE'])
def eliminar_usuario(id_user):
    return UsuarioController.eliminar_usuario(id_user)

@cross_origin()
@users.route('/restaurar_usuario/<id_user>', methods=['DELETE'])
def restaurar_usuario(id_user):
    return UsuarioController.restaurar_usuario(id_user)