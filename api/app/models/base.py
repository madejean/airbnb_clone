from peewee import *
from datetime import datetime
import config

db = MySQLDatabase(
        host = config.DATABASE['host'],
        port = congig.DATABASE['port'],
        user = config.DATABASE['user'],
        password = config.DATABASE['password'],
        database = config.DATABASE['database'],
        charset = config.DATABASE['charset']
)

class BaseModel(peewee.Model):
        id = PrimaryKeyField(unique = True)
        create_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')
        updated_at = DateTimeField(default=datetime.now, formats='%Y-%m-%d %H:%M:%S')

        def save(self, *args, **kwargs):
                self.updated_at = datetime.now
                return super(BaseModel, self).save(*args, **kwargs)
        
        def to_hash(self, values):
                values['id'] = self.id
                try:
                        values['created_at'] = self.created_at.strftime("%Y/%m/%d %H:%M:%S")
                except:
                        values['created_at'] = self.created_at
                try:
                        values['updated_at'] = self.updated_at.strftime("%Y/%m/%d %H:%M:%S")
                except:
                        values['updated_at'] = self.updated_at
                return values
                
class Meta:
        database = db
        order_by = ("id", )
