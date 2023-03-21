from flask import jsonify, request
from models.Factura_detalles import *

def artiuculosDeFactura(id_fac_enc): #Buscar aritculos de una factura - Factura detalles
    try:
        facDet = Factura_detalles.query.filter_by(id_fac_enc=id_fac_enc).all()
        if not facDet:
            return jsonify({'message': 'No hay factura detalles'}) , 404
        else:
            toFacturaDet = [registro.getDatos() for registro in facDet]
            return jsonify(toFacturaDet)
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()

