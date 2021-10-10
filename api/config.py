

class Config:
     from api import secrets
     #connect db
     test_conn = 'postgresql://{0}:{1}@{2}/{3}'.format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
     prod_conn = secrets.prod_uri

     SECRET_KEY = secrets.SuperSecretKey
     SQLALCHEMY_DATABASE_URI = prod_conn
     SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #handle token and auth
     JWT_SECRET_KEY = secrets.jwt_key
     JWT_ACCESS_TOKEN_EXPIRES = secrets.jwt_time
   
