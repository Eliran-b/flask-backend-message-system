from datetime import timedelta
from api import secrets
import os


class Config:
     #connect db
    conn = 'postgresql://{0}:{1}@{2}/{3}'.format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
    SECRET_KEY = secrets.SuperSecretKey
    SQLALCHEMY_DATABASE_URI = conn
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #handle token and auth
    JWT_SECRET_KEY = secrets.jwt_key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
   
