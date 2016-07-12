from peewee import *

class PlaceAminities(peewee.Model):
    place = ForeignKeyField('Place')
    amenity = ForeignKeyField('Amenity')

class Meta:
        database = db

