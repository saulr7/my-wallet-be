from flask import Blueprint, render_template, jsonify, request
from app.services import categories_service

category_routes = Blueprint('category_routes', __name__,  template_folder='')

@category_routes.route('/categoriesByUser/<useruid>')
def categories(useruid):
    try :
        data = categories_service.get_categories(useruid)
        auth_header = request.headers.get('Authorization')
        return data
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        return resp, 400

