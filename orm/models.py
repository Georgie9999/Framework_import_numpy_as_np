from collections import OrderedDict

from manager import Manager


class Field:
    pass


class IntegerField(Field):
    pass


class CharField(Field):
    pass


class BaseModel(type):
    """Metaclass for all models"""

    def __new__(mcs, class_name, bases, classdict, **kwargs):
        fields = OrderedDict()
        for key, value in classdict.items():
            if isinstance(value, Field):
                fields[key] = value
                classdict[key] = None
        cls = super(BaseModel, mcs).__new__(mcs, class_name, bases, classdict, **kwargs)
        setattr(cls, "_model_name", classdict["__qualname__"].lower())
        setattr(cls, "_original_fields", fields)
        setattr(cls, "objects", Manager(cls))
        return cls


class Model(metaclass=BaseModel):
    pass


class SomeModel(Model):
    id = IntegerField()
    name = CharField()


if __name__ == "__main__":
    model = SomeModel()
    print(model._model_name, model._original_fields)
