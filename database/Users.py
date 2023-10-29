import datetime
import mongoengine

class Users(mongoengine.Document):
  registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
  name = mongoengine.StringField(required = True)
  email = mongoengine.StringField(required = True)
  password = mongoengine.StringField(required = True)

  


  meta = {
    'db_alias': 'core',
    'collection': 'Users'
  }