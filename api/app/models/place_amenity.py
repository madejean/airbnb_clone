from peewee import *
from base import *
from place import *
from amenity import *

class PlaceAminities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

class Meta:
        database = db

