import deploy

class Config:
     #connect db
     test_conn = 'postgresql://{0}:{1}@{2}/{3}'.format(deploy.dbuser, deploy.dbpass, deploy.dbhost, deploy.dbname)
     prod_conn = deploy.prod_uri

     SECRET_KEY = deploy.SuperSecretKey
     SQLALCHEMY_DATABASE_URI = prod_conn
     SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #handle token and auth
     JWT_SECRET_KEY = deploy.jwt_key
     JWT_ACCESS_TOKEN_EXPIRES = deploy.jwt_time
   
