from abc import ABC, abstractmethod

from backend.shared.domain import exceptions


class DomainEntity(ABC):
    __id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if self.__id is not None:
            raise exceptions.EntityIdentifierAlreadySetError
        if not self._is_identifier_value_valid(value):
            raise exceptions.EntityIdentifierValueError

        self.__id = value

    @classmethod
    @abstractmethod
    def create_from_dict(cls, entity_data: dict):
        pass

    @property
    @abstractmethod
    def as_dict(self) -> dict:
        pass

    @staticmethod
    def _is_identifier_value_valid(value):
        if value in [0, '']:
            return False
        return True
