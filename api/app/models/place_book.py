from peewee import *
import datetime

class PlaceBook(BaseModel):
    place = ForeignKeyField('Place')
    user = ForeignKeyField('User')
    is_validated = BooleanField(default = False)
    date_start = datetime(null = False)
    number_nights = IntegerField(default = 1)
