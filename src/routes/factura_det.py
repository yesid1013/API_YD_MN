from controllers import FacturaDetController
from flask import Blueprint
from flask_cors import cross_origin
facDet = Blueprint('facDet',__name__)

@cross_origin()
@facDet.route('/facturasDet/<id_fac_enc>')
def facturasDet(id_fac_enc):
    return FacturaDetController.artiuculosDeFactura(id_fac_enc)
