from flask import jsonify, request
from models.Stock_detalles import *
from models.Stock_encabezado import Stock_encabezado
from models.Productos import Productos

def agregar_stock_det(id_stock_enc):
    try:
        stock_enc = Stock_encabezado.query.get(id_stock_enc)
        if not stock_enc:
            return jsonify({"message" : "No se encontro el stock encabezado"})
        else:
            id_producto = request.json['id_producto']
            cantidad = request.json['cantidad']
            new_stockdet = Stock_detalles(id_stock_enc,id_producto,cantidad)
            db.session.add(new_stockdet)
            db.session.commit()
            db.session.close()
            return jsonify({"message" : "Insercion de producto exitoso", "status" : 200})


    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def productos_en_local(id_stock_enc): #consulta para ver el stock de un local especifico
    try:
        lista =[]
        stock = db.session.query(Productos.nombre,Productos.precio,Stock_detalles.cantidad).filter(Stock_detalles.id_producto==Productos.id_producto,Stock_encabezado.id_stock_enc==Stock_detalles.id_stock_enc,Stock_encabezado.id_stock_enc==id_stock_enc, Stock_detalles.estado==1).all()

        for producto in stock:
            contenido = {"Nombre" : producto.nombre, "Precio" : producto.precio, "Cantidad" : producto.cantidad}
            lista.append(contenido)
        
        header =request.headers.get('authorization')
        print(header)

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
            return jsonify({"Message" : "Stock no encontrado"}) , 404
        else:
            stock.cantidad = request.json['cantidad']
            db.session.commit()
            return jsonify({"Message" : "Producto actualizado"}) , 200

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()

def eliminar_producto(id_stock_det): #Cambiar el estado del producto a 0
    try:
        producto = Stock_detalles.query.get(id_stock_det)
        if not producto:
            return jsonify({"Message" : "Producto no encontrado"}) , 404
        else:
            producto.estado = 0
            db.session.commit()
            return jsonify({"Message" : "Producto eliminado"})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    
    finally:
        db.session.close()
    




