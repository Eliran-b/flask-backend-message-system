from resources.message import MessageRes, MessageCollection
from resources.user import UserRegister, UserLogin
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
from security import bcrypt
from datetime import timedelta


app = Flask(__name__)


app.config['SECRET_KEY'] = '30674835a84a7d369254e954'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gscnlevfjbncbh:43af4cc79385119f7d3287cd418d4e02ec48175e72b9752516af8abc786f8999@ec2-34-193-101-0.compute-1.amazonaws.com:5432/d24a6l5s58rhcd"
app.config['JWT_SECRET_KEY'] = "ajdshkjfh.sjuhkfuhsf.sjddhjfsh"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
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


