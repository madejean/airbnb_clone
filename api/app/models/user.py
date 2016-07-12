from peewee import *
import md5

class User(BaseModel):
    email = CharField(128, null = False, unique = True)
    password = CharField(128, null = False)
    first_name = CharField(128, null = False)
    last_name = CharField(128, null = False)
    is_admin = BooleanField(default = False)
    
def set_password(self, clear_password):
    clear_password = password
    m = md5.new()
    m.update(password)
    m.digest
