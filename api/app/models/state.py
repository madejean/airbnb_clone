from peewee import *

class User(BaseModel):
    name = CharField(128, null = False, unique = True)
