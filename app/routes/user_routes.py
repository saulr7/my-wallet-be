from flask import Blueprint, render_template, jsonify, request
from app.services import user_service

user_routes = Blueprint('user_routes', __name__,  template_folder='')

@user_routes.route('/addUser', methods= ['POST'])
def add_user():
    try :
        if request.method == 'POST':
            user = request.get_json()
            data = user_service.add_user(user)
            return data
        else:
            return "", 400
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        print(e)
        return resp, 400
