from flask import jsonify, request
from models.Clientes import *

def agregarCliente():
    try:
        num_documento = request.json['num_documento']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        telefono = request.json['telefono']
        email = request.json['email']

        new_cliente = Clientes(num_documento,nombre,apellido,telefono,email)

        db.session.add(new_cliente)
        db.session.commit()

        return jsonify({"message": "Cliente insertado ", "status" : 200})

    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})

def listar_clientes():
    try:
        clientes = Clientes.query.filter_by(estado=1).all()
        if not clientes:
            return jsonify({'message': 'No hay clientes'}), 404
        else:
            toclientes = [cliente.getDatos() for cliente in clientes]
            return jsonify(toclientes)
            
    except Exception as e:
        return jsonify({"Ha ocurrido un error" : str(e)})
