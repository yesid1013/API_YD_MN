from flask import Blueprint
from controllers import loginController
from flask_cors import cross_origin

login_ = Blueprint('login',__name__)

@cross_origin()
@login_.route('/login', methods=['POST'])
def login():
    return loginController.login()

@cross_origin()
@login_.route('/logout', methods = ['POST'])
def logout():
    return loginController.logout()