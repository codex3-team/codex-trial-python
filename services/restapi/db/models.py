
from peewee import *
from db.db import init_db
import uuid

db = init_db()
print(db)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class CarsModel(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    make = CharField(128)
    model = CharField(128)
    year = CharField(4)

    class Meta:
    	table_name = 'cars'

try:
	CarsModel.create_table()
except Exception as e:
	print(e)


