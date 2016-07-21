from base import *
from peewee import *

class State(BaseModel):
    name = CharField(128, null = False, unique = True)

    def to_hash(self):
        values = {
            'name': self.name
        }
        return super(State, self).to_hash(values)
    
