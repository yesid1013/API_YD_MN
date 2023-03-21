from flask import jsonify, request
from models.Factura_encabezado import *
from models.Clientes import Clientes

def buscar_facturas(): #Consulta de las facturas encabezado
    try:
        factura_enc = db.session.query(Factura_encabezado).filter(Clientes.id_cliente==Factura_encabezado.id_cliente)
        if not factura_enc:
            return jsonify({'message': 'no hay factura encabezado'})
        else:
            toFactura = [registro.getDatos() for registro in factura_enc]
            return jsonify(toFactura)
            
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})