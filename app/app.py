from flask import Flask
from routes import routes , user_routes, transaction_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(routes.category_routes)
    app.register_blueprint(user_routes.user_routes)
    app.register_blueprint(transaction_routes.transaction_routes)

    @app.route('/', methods=['GET'])
    def index():
        print("Here")
        return "Test", 200

    if __name__ == "__main__":
        # app.run(debug= True, port= 5002)
        app.run()

    return app

app = create_app()