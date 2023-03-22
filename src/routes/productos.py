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