from flask import Flask,jsonify
from utils.db import db
from controllers import UsuarioController
from routes.usuario import users
from routes.stock_detalles import stockDet
from routes.login import login_
from routes.factura_enc import facEnc
from routes.factura_det import facDet
from routes.productos import products
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_SECRET_KEY"] = "Proyecto_tecnologo"

jwt = JWTManager(app)

db.init_app(app)


app.register_blueprint(users)
app.register_blueprint(stockDet)
app.register_blueprint(login_)
app.register_blueprint(facEnc)
app.register_blueprint(facDet)
app.register_blueprint(products)






def pagina_no_encontrada(error):
    return jsonify({"message" : "Pagina no encontrada"})



if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(debug=True)