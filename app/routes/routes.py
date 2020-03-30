from flask import Blueprint, render_template, jsonify, request
from app.services import categories_service

category_routes = Blueprint('category_routes', __name__,  template_folder='')

@category_routes.route('/categoriesByUser/<useruid>')
def categories(useruid):
    try :
        print(useruid)
        data = categories_service.get_categories(useruid)
        auth_header = request.headers.get('Authorization')
        print(data)
        return data
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        return resp, 400

@category_routes.route('/addCategory' , methods=['POST'])
def addCategory():
    try :
        if request.method == 'POST':
            category = request.get_json()
            data = categories_service.add_category(category)
            return "added"
        else:
            return "", 400
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        return resp, 400

@category_routes.route('/removeCategory/<int:categoryId>/<useruid>' ,methods=['GET'])
def removeCategory(categoryId, useruid):
    try :
        data = categories_service.remove_category(categoryId, useruid)
        return data
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        return resp, 400

