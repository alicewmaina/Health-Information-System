from flask import Flask

app = Flask(__name__)

def create_app():
    from app.routes import register_routes
    register_routes(app)
    return app