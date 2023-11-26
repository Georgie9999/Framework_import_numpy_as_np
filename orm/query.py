from typing import Any
from abc import abstractmethod


AND = "and"
OR = "or"


class Q:

    def __init__(self, op_type: str = AND, **kwargs) -> None:
        self.separator = op_type
        self._params = kwargs

    def __str__(self) -> str:
        kv_pairs = [f"{k} = {v}" for k, v in self._params.items()]
        return f" {self.separator}".join(kv_pairs)
    
    def __bool__(self) -> bool:
        return bool(self._params)


class BaseStatement:
    name = None

    @abstractmethod
    def add(self, *args: Any, **kwargs: Any):
        pass

    def definition(self) -> str:
        return self.name + "\n\t" + self.line() + "\n"

    @abstractmethod
    def line(self) -> str:
        pass
    
    @abstractmethod
    def __bool__(self) -> bool:
        pass


class Select(BaseStatement):
    name = "SELECT"

    def __init__(self) -> None:
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(*args)

    def line(self) -> str:
        separator = ","
        return separator.join(self._params)
    
    def __bool__(self) -> bool:
        return bool(self._params)


class From(BaseStatement):
    name = "FROM"

    def __init__(self) -> None:
        self._params = []

    def add(self, *args, **kwargs):
        self._params.extend(*args)

    def line(self) -> str:
        separator = ","
        return separator.join(self._params)
    
    def __bool__(self) -> bool:
        return bool(self._params)
    

class Where(BaseStatement):
    name = "WHERE"

    def __init__(self, op_type: str = AND, **kwargs) -> None:
        self._q = Q(op_type, **kwargs)

    def add(self, op_type: str = AND, **kwargs):
        self._q = Q(op_type, **kwargs)
        return self._q

    def line(self) -> str:
        return str(self._q)
    
    def __bool__(self) -> bool:
        return bool(self._q)