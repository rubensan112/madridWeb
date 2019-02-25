"""
User domain repository contract (to be implemented in another layer)
"""
from abc import ABC, abstractmethod
from typing import List

from backend.authentication.domain.entities import User
from backend.shared.domain.entities import DomainEntity
from backend.shared.infrastructure.repositories import EntityRepository


class UserRepository(EntityRepository, ABC):
    @abstractmethod
    def find_one_by_id(self, entity_id) -> User: pass

    @abstractmethod
    def find_by(self, **filter_params) -> List[User]: pass

    @abstractmethod
    def save(self, entity: DomainEntity): pass
