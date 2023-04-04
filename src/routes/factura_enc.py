from flask import Blueprint
from controllers import FacturaEncController
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required,get_jwt_identity


facEnc = Blueprint('facEnc',__name__)

@cross_origin()
@facEnc.route('/facturas_enc')
def facturas_enc():
    return FacturaEncController.buscar_facturas()

@cross_origin()
@facEnc.route('/ultima_facturas_enc')
def ultima_facturas_enc():
    return FacturaEncController.ultima_factura()

@cross_origin()
@facEnc.route('/insertar_factEncabezado', methods = ['POST'])
@jwt_required
def insertar_factEncabezado():
    current_user_id = get_jwt_identity()
    return FacturaEncController.insertar_factEncabezado(current_user_id)