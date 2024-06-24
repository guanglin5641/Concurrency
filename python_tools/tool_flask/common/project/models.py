from peewee import Model, CharField, IntegerField
from config import db

class BaseModel(Model):
    class Meta:
        database = db

class ZeroProduct(BaseModel):
    name = CharField(max_length=50)
    description = CharField(max_length=255)


class AnotherTable(BaseModel):
    column1 = IntegerField()
    column2 = CharField(max_length=255)
