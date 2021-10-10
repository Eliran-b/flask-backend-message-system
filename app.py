from api import create_app, api, jwt
from api.resources.message import MessageRes, MessageCollection
from api.resources.user import UserRegister, UserLogin

app = create_app

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
    from api.models.user import User
    return User.query.filter_by(username=identity).one_or_none()




if __name__ == '__main__':
    app.run()
    #app.run(debug=True)  


