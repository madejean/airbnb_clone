from peewee import *
from datetime import datetime

db = MySQLDatabase(
        host = DATABASE['host'],
        port = DATABASE['port'],
        user = DATABASE['user'],
        password = DATABASE['password'],
        database = DATABASE['database'],
        charset = DATABASE['charset']
)

class BaseModel(peewee.Model):
        id = PrimaryKeyField(unique = True)
        create_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
        updated_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')

        def save(self, *args, **kwargs):
                self.updated_at = datetime.now
                peewee.Model.save(self)
                
class Meta:
        database = db
        order_by = ("id", )
