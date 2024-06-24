from peewee import Model
from playhouse.shortcuts import model_to_dict

class DatabaseHelper:
    def __init__(self, model):
        if not issubclass(model, Model):
            raise ValueError("model must be a subclass of peewee.Model")
        self.model = model

    def add(self, **data):
        return self.model.create(**data)

    def get(self, record_id):
        try:
            return self.model.get(self.model.id == record_id)
        except self.model.DoesNotExist:
            return None

    def get_all(self):
        return list(self.model.select())

    def update(self, record_id, **data):
        query = self.model.update(**data).where(self.model.id == record_id)
        return query.execute()

    def delete(self, record_id):
        query = self.model.delete().where(self.model.id == record_id)
        return query.execute()

    def to_dict(self, instance):
        return model_to_dict(instance)
