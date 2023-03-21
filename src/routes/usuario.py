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