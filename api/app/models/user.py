from peewee import *
from base import *
from hashlib import md5

class User(BaseModel):
    email = CharField(128, null = False, unique = True)
    password = CharField(128, null = False)
    first_name = CharField(128, null = False)
    last_name = CharField(128, null = False)
    is_admin = BooleanField(default = False)
    
    def set_password(self, clear_password):
        m = md5()
        m.update(clear_password)
        return m.hexdigest()
    
    def to_hash(self):
        values = {
            'first_name': self.first_name,
            'email': self.email,
            'last_name': self.last_name,
            'is_admin': self.is_admin
        }
        return super(User, self).to_hash(values)
