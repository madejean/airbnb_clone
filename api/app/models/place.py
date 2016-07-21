from peewee import *
from base import *
from user import *
from city import *

class Place(BaseModel):
    owner = ForeignKeyField(User, related_name = 'places')
    city = ForeignKeyField(City, related_name = 'places')
    name = CharField(128, null = False)
    description = TextField()
    number_rooms = IntegerField(defautlt = 0)
    numbert_bathrooms = IntegerField(default = 0)
    max_guest = IntegerField(default = 0)
    price_by_night = IntegerField(default = 0)
    latitude = FloatField()
    longitude = FloatField()

    def to_hash(self):
        city = City.get(City.id == self.city)
        owner = User.get(User.id == self.owner)
        values = {
            'number_bathrooms': self.number_bathrooms,
            'max_guest': self.max_guest,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'owner_id': owner.id,
            'city_id': city.id,
            'name': self.name,
            'description': self.description,
            'number_rooms': self.number_rooms
        }
        return super(Place, self).to_hash(values)
