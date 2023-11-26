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
    
    def update(self, new_data):
        fields = new_data.keys()
        placeholder_format = ', '.join([f'{field_name} = %s' for field_name in fields])
        query = f"UPDATE {self.model._model_name} SET {placeholder_format}"
        params = list(new_data.values())
        self._connector.execute_query(query, params)

    def delete(self):
        query = f"DELETE FROM {self.model_class.table_name} "
        self._connector.execute_query(query)
    
    def fetch(self):
        query = str(self.query)
        db_response = self._connector.execute_query(query).fetch_all()
        result = []
        for row in db_response:
            model = self.model()
            for field, value in zip(self._model_fields, row):
                setattr(model, field, value)
            result.append(model)

        return result