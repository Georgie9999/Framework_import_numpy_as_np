import sqlite3


class DBConnector:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(DBConnector, cls).__new__(cls, *args, **kwargs)
        return cls.instance
    
    def __init__(self) -> None:
        self._connection = sqlite3.connect("some_database.db")

    def fetch(self, query):
        cursor = self._connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()