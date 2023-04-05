from flask import jsonify, request
from models.Factura_encabezado import *
from models.Locales import Locales
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

def insertar_factEncabezado(id_user):
    try:
        id_local = db.session.query(Locales.id_local).filter(Locales.id_user==id_user).first()
        id_cliente = request.json['id_cliente']
        precio_total = request.json['precio_total']

        new_factEnc = Factura_encabezado(id_local.id_local,id_cliente,precio_total)

        db.session.add(new_factEnc)
        db.session.commit()

        return jsonify({"message": "Factura encabezado insertado", "status" : 200})
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def ultima_factura():
    try:
        db.session.commit()
        factura = Factura_encabezado.query.order_by(Factura_encabezado.id_fac_enc.desc()).first()
        datos = {"id_fac_enc" : factura.id_fac_enc, "id_local" : factura.id_local, "id_cliente" : factura.id_cliente, "fecha" : factura.fecha, "precio_total" : factura.precio_total }
        return factura.id_fac_enc

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def id_local():
    try:
        factura = Factura_encabezado.query.order_by(Factura_encabezado.id_fac_enc.desc()).first()

        return factura.id_local
        
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    