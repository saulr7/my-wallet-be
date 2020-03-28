from flask import Blueprint, render_template, jsonify
from services import categories_service

category_routes = Blueprint('category_routes', __name__,  template_folder='')

@category_routes.route('/categories')
def categories():
    try :
        data = categories_service.get_categories()
        return data
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        return resp, 400

