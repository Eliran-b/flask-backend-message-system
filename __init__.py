from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config
from db import db

api = Api()
jwt = JWTManager()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)

    
    
    return app