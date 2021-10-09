#automation scripts
from api import app


@app.cli.command("script")
def execute_script():
    print('Script Executing....')
    print()
    #create a random secret key of hexadecimal value
    #import os
    #print(os.urandom(12).hex())
    '''
    from api import db
    from api.models.user import User
    from api.models.message import Message
    from api.models.receiver import Receiver 
    db.drop_all()
    db.create_all()
    db.session.commit()
    '''
    