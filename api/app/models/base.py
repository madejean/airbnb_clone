import peewee
import datetime

db = SqliteDatabase('my_models.db', pragmas = (
    ('foreign_keys', True),
))

class BaseModel(peewee.Model):
        id = PrimaryKeyField(unique = True)
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()

        def save(self, *args, **kwargs):
                self.updated_at = updated_at
        
class Meta:
        database = db
        order_by = ("id", )
