from datetime import timedelta

#production DB URI
prod_uri = "postgres://gscnlevfjbncbh:43af4cc79385119f7d3287cd418d4e02ec48175e72b9752516af8abc786f8999@ec2-34-193-101-0.compute-1.amazonaws.com:5432/d24a6l5s58rhcd"


#host name
dbhost = 'localhost'

#host name
dbuser = 'eli'

#password
dbpass = 'msgsys123!'

#database name
dbname = 'messages_system'

#secret key for user validation
SuperSecretKey = '30674835a84a7d369254e954'

#JSON Web Token
jwt_key = "ajdshkjfh.sjuhkfuhsf.sjddhjfsh"

#JWT time
jwt_time = timedelta(minutes=15)