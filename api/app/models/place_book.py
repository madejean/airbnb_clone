from peewee import *
from base import * 
from user import *
from place import *

class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name = "places_booked")
    is_validated = BooleanField(default = False)
    date_start = DateTimeField(null = False)
    number_nights = IntegerField(default = 1)

    def to_hash(self):
        place = Place.get(Place.id == self.place)
        user = User.get(User.id = self.user)
        values = {
            'place_id': place.id,
            'user_id' : user.id,
            'is_validated': self.is_validated,
            'date_start': self.date_start.strftime("%Y/%m/%d %H:%M:%S"),
            'number_nights': self.number_nights
        }
        return super(PlaceBook, self).to_hash(values)
