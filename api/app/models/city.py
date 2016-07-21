from peewee import *
from base import *
from state import *
from playhouse.shorcuts import model_to_dict

class City(BaseModel):
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name = "cities", on_delete='CASCADE')

    def to_hash(self):
        state  = State.get(State.id == self.state)
        values = {
            "name": self.name,
            "state_id": state.id
        }
        return super(City, self).to_hash(values)
