from flask import jsonify, request
from models.Factura_detalles import *
from models.Stock_detalles import Stock_detalles
from models.Stock_encabezado import Stock_encabezado
from models.Productos import Productos
from controllers import FacturaEncController

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

def insertar_facturaDet():
    try:

        id_fac_enc = FacturaEncController.ultima_factura() #Buscar ultima factura
        id_producto = request.json['id_producto']
        precio = request.json['precio']
        cantidad = request.json['cantidad']

        newFactDet = Factura_detalles(id_fac_enc,id_producto,precio,cantidad) #agregar factura detalle
        db.session.add(newFactDet)

        id_local = FacturaEncController.id_local()

        stock_enc = db.session.query(Stock_encabezado.id_stock_enc).filter(Stock_encabezado.id_local== id_local).first()


        producto = db.session.query(Stock_detalles.id_stock_det,Productos.nombre,Productos.precio,Stock_detalles.cantidad).filter(Stock_detalles.id_producto==Productos.id_producto, Stock_encabezado.id_stock_enc==Stock_detalles.id_stock_enc,Stock_encabezado.id_stock_enc == stock_enc.id_stock_enc, Productos.id_producto == id_producto).first()

        stockdet = db.session.query(Stock_detalles).filter_by(id_stock_det=producto.id_stock_det).first()

        stockdet.cantidad -= cantidad

        
        db.session.commit()


        return jsonify({"message": "Factura detalle insertada", "status" : 200})
    
    except Exception as e:
        return jsonify(e)

