import sqlite3


class DBConnector:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(DBConnector, cls).__new__(cls, *args, **kwargs)
        return cls.instance
    
    def __init__(self) -> None:
        self._connection = sqlite3.connect("some_database.db")

    def _get_cursor(self):
        return self._connection.cursor()

    def execute_query(self, query, params=None):
        cursor = self._get_cursor()
        cursor.execute(query, params)
