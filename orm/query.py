from typing import Any
from abc import abstractmethod


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
