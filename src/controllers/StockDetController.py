from flask import jsonify, request
from models.Stock_detalles import *
from models.Stock_encabezado import Stock_encabezado
from models.Productos import Productos
from models.Locales import Locales

def agregar_stock_det(id_user): #agregar producto al stock
    try:
        id_local = db.session.query(Locales.id_local).filter(Locales.id_user==id_user).first()
        id_stock_enc = db.session.query(Stock_encabezado.id_stock_enc).filter(Stock_encabezado.id_local== id_local.id_local).first()
        
        id_producto = request.json["id_producto"]
        cantidad = request.json['cantidad']

        producto = Stock_detalles.query.filter_by(id_stock_enc=id_stock_enc.id_stock_enc,id_producto=id_producto,estado=1).first()

        if not producto:
            newproducto = Stock_detalles(id_stock_enc.id_stock_enc,id_producto,cantidad)
            db.session.add(newproducto)
            db.session.commit()
            return jsonify({"message" : "Producto insertado"})
        else:
            return jsonify({"message" : "El producto ya se encuentra en su stock"}) , 400

    except Exception as e:
        return jsonify({"message" : "Ha ocurrido un error", "error" : str(e)}) 

def productos_en_local(id_user): #consulta para ver el stock de un local especifico
    try:
        lista =[]

        id_local = db.session.query(Locales.id_local).filter(Locales.id_user==id_user).first()

        stock_enc = db.session.query(Stock_encabezado.id_stock_enc).filter(Stock_encabezado.id_local== id_local.id_local).first()


        stock = db.session.query(Stock_detalles.id_stock_enc,Stock_detalles.id_stock_det,Productos.nombre,Productos.precio,Stock_detalles.cantidad).filter(Stock_detalles.id_producto==Productos.id_producto,Stock_encabezado.id_stock_enc==Stock_detalles.id_stock_enc,Stock_encabezado.id_stock_enc==stock_enc.id_stock_enc, Stock_detalles.estado==1).all()

        for producto in stock:
            contenido = {"id_stock_enc" : producto.id_stock_enc,"id_stock_det":producto.id_stock_det,"Nombre" : producto.nombre, "Precio" : producto.precio, "Cantidad" : producto.cantidad}
            lista.append(contenido)
        
        return jsonify(lista)

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

    finally:
        db.session.close()


def productos_en_local_borrados(id_user): #consulta para ver el stock de un local especifico
    try:
        lista =[]

        id_local = db.session.query(Locales.id_local).filter(Locales.id_user==id_user).first()

        stock_enc = db.session.query(Stock_encabezado.id_stock_enc).filter(Stock_encabezado.id_local== id_local.id_local).first()


        stock = db.session.query(Stock_detalles.id_stock_enc,Stock_detalles.id_stock_det,Productos.nombre,Productos.precio,Stock_detalles.cantidad).filter(Stock_detalles.id_producto==Productos.id_producto,Stock_encabezado.id_stock_enc==Stock_detalles.id_stock_enc,Stock_encabezado.id_stock_enc==stock_enc.id_stock_enc, Stock_detalles.estado==0).all()

        for producto in stock:
            contenido = {"id_stock_enc" : producto.id_stock_enc,"id_stock_det":producto.id_stock_det,"Nombre" : producto.nombre, "Precio" : producto.precio, "Cantidad" : producto.cantidad}
            lista.append(contenido)
        
        return jsonify(lista)

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

    finally:
        db.session.close()


def producto_especifico(): #Buscar un producto especifico en una tienda
    try:
        producto = db.session.query(Productos.nombre,Productos.precio,Stock_detalles.cantidad).filter(Stock_detalles.id_producto==Productos.id_producto, Stock_encabezado.id_stock_enc==Stock_detalles.id_stock_enc,Stock_encabezado.id_stock_enc == 1, Productos.id_producto == 4).first()

        return jsonify({"Nombre" : producto[0], "Precio": producto[1], "Cantidad" : producto[2]})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

    finally:
        db.session.close()

def editar_stock(id_stock_det): #Actualizar cantidad de un producto en el stock
    try:
        stock = Stock_detalles.query.get(id_stock_det)
        if not stock:
            return jsonify({"message" : "Stock no encontrado"}) , 404
        else:
            stock.cantidad = request.json['cantidad']
            db.session.commit()
            return jsonify({"message" : "Producto actualizado"}) , 200

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()

def eliminar_producto(id_stock_det): #Cambiar el estado del producto a 0
    try:
        producto = Stock_detalles.query.get(id_stock_det)
        if not producto:
            return jsonify({"message" : "Producto no encontrado"}) , 404
        else:
            producto.estado = 0
            db.session.commit()
            return jsonify({"message" : "Producto eliminado"})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()

def restaurar_producto(id_stock_det): #Cambiar el estado del producto a 1
    try:
        producto = Stock_detalles.query.get(id_stock_det)
        if not producto:
            return jsonify({"message" : "Producto no encontrado"}) , 404
        else:
            producto.estado = 1
            db.session.commit()
            return jsonify({"message" : "Producto restaurado"})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()
    




