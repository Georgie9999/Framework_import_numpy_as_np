from parser.Parser import Parser


class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0
    def __str__(self):
        return f"{self.name=},{self.age=}, {self.height=}"
temp = Parser()
person = temp.parse_data_model(b'{"name": "Serega", "age": 15, "height":190}', Person())
print(person)
