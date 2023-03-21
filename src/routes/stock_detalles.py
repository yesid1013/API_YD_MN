from flask import Blueprint
from controllers import StockDetController
from models.Usuario import Usuario
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_cors import cross_origin

stockDet = Blueprint('stockDet',__name__)
@cross_origin()
@stockDet.route('/add_stockDet/<id_stock_enc>',methods =['POST'])
def add_stockdetalles(id_stock_enc):
    return StockDetController.agregar_stock_det(id_stock_enc)

@cross_origin()
@stockDet.route('/stock_local/<id_stock_enc>',methods =['GET'])
@jwt_required
def stock_de_un_local(id_stock_enc):
    #current_user_id = get_jwt_identity()
    #user = Usuario.query.get(current_user_id)
    #if user.cargo!=1:
        #return "Acceso denegado"
    
    return StockDetController.productos_en_local(id_stock_enc)

@cross_origin()
@stockDet.route('/producto_en_local')
def producto_en_local():
    return StockDetController.producto_especifico()

@cross_origin()
@stockDet.route('/actualizar_stock/<id_stock_det>', methods = ['PUT'])
def actualizar_stock(id_stock_det):
    return StockDetController.editar_stock(id_stock_det)

@cross_origin()
@stockDet.route('/eliminar_producto/<id_stock_det>', methods = ['DELETE'])
def eliminar_producto(id_stock_det):
    return StockDetController.eliminar_producto(id_stock_det)