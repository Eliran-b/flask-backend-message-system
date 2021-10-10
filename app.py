from resources.message import MessageRes, MessageCollection
from resources.user import UserRegister, UserLogin
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
from security import bcrypt
from conf import SuperSecretKey, prod_uri, jwt_key, jwt_time

app = Flask(__name__)

#This data will be encrypted on the vm
app.config['SECRET_KEY'] = SuperSecretKey
app.config['SQLALCHEMY_DATABASE_URI'] = prod_uri
app.config['JWT_SECRET_KEY'] = jwt_key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_time
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)
jwt = JWTManager(app)


db.init_app(app)
bcrypt.init_app(app)





api.add_resource(UserRegister, "/register", "/register/<string:username>/<string:password>")
api.add_resource(UserLogin, "/login", "/login/<string:username>/<string:password>")

api.add_resource(MessageRes, "/message", "/message/<string:receivers_username>/<string:message_body>/<string:message_subject>")
api.add_resource(MessageCollection, "/messages")

#login user
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user["username"]

#activate every request when jwt is required 
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    from models.user import User
    return User.query.filter_by(username=identity).one_or_none()


    



if __name__ == '__main__':
    app.run()
    #app.run(debug=True)  


