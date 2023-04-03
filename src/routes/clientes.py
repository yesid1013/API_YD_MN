from flask import Blueprint
from flask_cors import cross_origin
from controllers import ClienteController

cliente = Blueprint('cliente',__name__)

@cross_origin()
@cliente.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    return ClienteController.agregarCliente()

@cross_origin()
@cliente.route('/listar_clientes', methods=['GET'])
def listar_clientes():
    return ClienteController.listar_clientes()