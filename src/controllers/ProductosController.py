from flask import jsonify, request
from models.Productos import *

def agregar_producto():
    try:
        num_serie = request.json['num_serie']
        nombre = request.json['nombre']
        tipo_producto = request.json['tipo_producto']
        precio = request.json['precio']

        new_producto = Productos(num_serie,nombre,tipo_producto,precio)

        db.session.add(new_producto)
        db.session.commit()

        return jsonify({"message": "Producto insertado insertado", "status" : 200})
    
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
    

def get_productos():
    try: 
        lista = []
        allproducts = db.session.query(Productos.nombre,Productos.num_serie,Productos.id_tipo_producto,Productos.precio).filter(Productos.estado==1).all()
        
        for producto in allproducts:
            datos ={"Nombre":producto.nombre, "Num_serie":producto.num_serie,"Id_tipo_producto":producto.id_tipo_producto ,"Precio" : producto.precio }
            lista.append(datos)
        
        return jsonify(lista)

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

    finally:
        db.session.close()
        


        