from flask import Blueprint
from controllers import ProductosController
from flask_cors import cross_origin

products = Blueprint('products', __name__)

@cross_origin()
@products.route('/agregar_producto', methods=['POST'])
def usuarios():
    return ProductosController.agregar_producto()