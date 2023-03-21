from flask import Blueprint
from controllers import FacturaEncController
from flask_cors import cross_origin

facEnc = Blueprint('facEnc',__name__)

@cross_origin()
@facEnc.route('/facturas_enc')
def facturas_enc():
    return FacturaEncController.buscar_facturas()