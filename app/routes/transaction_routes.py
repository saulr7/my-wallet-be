from flask import Blueprint, render_template, request
from app.services import transaction_services

transaction_routes = Blueprint('transaction_routes', __name__,  template_folder='')

@transaction_routes.route('/addTransaction', methods= ['POST'])
def add_transaction():
    try :
        if request.method == 'POST':
            trans = request.get_json()
            data = transaction_services.add_transaction(trans)
            return "added"
        else:
            return "", 400
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        print(e)
        return resp, 400

@transaction_routes.route('/getTransactionsByUser/<userid>')
def get_transaction(userid):
    try :
        data = transaction_services.get_transaction(userid)
        return data
    except Exception as e:
        resp = {
            "message" : "something went wrong" ,
            "err" :  str(e)
        }
        print(e)
        return resp, 400
