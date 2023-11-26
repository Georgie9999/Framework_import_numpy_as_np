from query import Query
from connector import DBConnector


class Manager:

    def __init__(self, model) -> None:
        self.model = model
        self._model_fields = model._original_fields.keys()
        query = Query()
        self.query = query.SELECT(*self._model_fields).FROM(model._model_name)
        self._connector = DBConnector()

    def filter(self, *args, **kwargs):
        self.query = self.query.WHERE(*args, **kwargs)
        return self
    
    def fetch(self):
        query = str(self.query)
        db_response = self._connector.fetch(query)
        result = []
        for row in db_response:
            model = self.model()
            for field, value in zip(self._model_fields, row):
                setattr(model, field, value)
            result.append(model)

        return result