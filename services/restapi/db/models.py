from peewee import Model
from db import init_db

db = init_db()


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db



