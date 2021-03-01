from peewee import *
from db.models import BaseModel
import uuid


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
