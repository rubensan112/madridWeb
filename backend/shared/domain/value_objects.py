from abc import ABC, abstractmethod


class ValueObject(ABC):
    @classmethod
    @abstractmethod
    def create_from_dict(cls, object_data: dict): pass

    @property
    @abstractmethod
    def as_dict(self) -> dict: pass
