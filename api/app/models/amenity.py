from peewee import *
from base import * 

class Amenity(BaseModel):
    name = CharField(128, null = False)

    def to_hash(self):
        values = {
            'name': self.name
        }
        return super(Amenity, self).to_hash(values)
