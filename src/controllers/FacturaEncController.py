from flask import jsonify, request
from models.Factura_encabezado import *
from models.Locales import Locales
from models.Clientes import Clientes
from datetime import datetime


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

def facturas_local(id_user):
    try:
        lista = []

        id_local = db.session.query(Locales.id_local).filter(Locales.id_user==id_user).first()


        facturas = db.session.query(Factura_encabezado.id_fac_enc,Clientes.nombre,Clientes.apellido,Clientes.num_documento, Factura_encabezado.fecha, Factura_encabezado.precio_total,Factura_encabezado.id_local).join(Clientes,Factura_encabezado.id_cliente==Clientes.id_cliente).filter(Factura_encabezado.id_local == id_local.id_local, Factura_encabezado.estado == 1).all()

        for factura in facturas:
            datos = {"id_fac_enc" : factura.id_fac_enc, "nombre" : factura.nombre, "apellido" : factura.apellido, "fecha" : factura.fecha, "precio_total" : factura.precio_total, "id_local" : factura.id_local, "num_documento" : factura.num_documento}
            lista.append(datos)
        
        return jsonify(lista)

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    

def get_facturas():
    try:
        lista = []
        facturas = db.session.query(Factura_encabezado.id_fac_enc,Clientes.nombre,Clientes.apellido,Clientes.num_documento, Factura_encabezado.fecha, Factura_encabezado.precio_total,Factura_encabezado.id_local, Locales.nombre.label("nombre_local")).join(Clientes,Factura_encabezado.id_cliente==Clientes.id_cliente).join(Locales, Factura_encabezado.id_local==Locales.id_local).filter(Factura_encabezado.estado == 1).all()

        for factura in facturas:
            fecha_formato = factura.fecha.strftime('%y/%m/%d %H:%M:%S')

            datos = {"id_fac_enc" : factura.id_fac_enc, "nombre" : factura.nombre, "apellido" : factura.apellido, "fecha" : fecha_formato, "precio_total" : factura.precio_total, "id_local" : factura.id_local, "num_documento" : factura.num_documento, "nombre_local":factura.nombre_local}
            lista.append(datos)
        
        return jsonify(lista)

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
