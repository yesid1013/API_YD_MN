from flask import Blueprint
from flask_jwt_extended import jwt_required
from controllers import ProductosController
from flask_cors import cross_origin

products = Blueprint('products', __name__)

@cross_origin()
@products.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    return ProductosController.agregar_producto()



@cross_origin()
@products.route('/obtener_productos', methods=['GET'])
@jwt_required
def obtener_productos():
    return ProductosController.get_productos()

@cross_origin()
@products.route('/actualizar_producto/<id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
    return ProductosController.editar_producto(id_producto)

@cross_origin()
@products.route('/eliminar_product/<id_producto>', methods=['DELETE'])
def eliminar_product(id_producto):
    return ProductosController.eliminar_producto(id_producto)