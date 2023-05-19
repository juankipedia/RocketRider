from typing import Any, Dict, Optional, Type, TypeVar, Generic

T = TypeVar("T")

class Factory(Generic(T)):
    def __init__(self, prototype: T) -> None:
        if type(prototype) is not type:
            raise ValueError("Argument prototype it not a data type")
        self._prototype = prototype

    def create(self, x: float, y: float, properties: Optional[Dict[str, Any]] = None):
        if properties is None:
            properties = {}

        if type(properties) is not dict:
            raise TypeError("Argument properties is not a dict")

        properties.update(dict(x=x, y=y))
        return self._prototype(**properties)