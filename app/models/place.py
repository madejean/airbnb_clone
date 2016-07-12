from peewee import *

class Place(BaseModel):
    owner = ForeignKeyField('User', related_name = 'places')
    city = ForeignKeyField('City', related_name = 'places')
    name = CharField(128, null = False)
    description = TextField()
    number_rooms = IntegerField(defautlt = 0)
    numbert_bathrooms = IntegerField(default = 0)
    max_guest = IntegerField(default = 0)
    price_by_night = IntegerField(default = 0)
    latitude = FloatField()
    longitude = FloatField()
