from flask import Blueprint

__author__ = 'dzhou'


store_blueprint = Blueprint('stores', __name__)

@store_blueprint.route('/store/<string:name>')
def store_page():
    pass
