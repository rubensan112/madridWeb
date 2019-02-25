"""Repository implementation for domain repository"""
from typing import Type

from backend.authentication.domain.repositories import UserRepository
from backend.authentication.models import UserORM
from backend.shared.infrastructure.mappers import EntityMapper
from backend.shared.infrastructure.repositories import DatabaseEntityRepository


class UserDatabaseRepository(DatabaseEntityRepository, UserRepository):
    entity_mapper: Type[EntityMapper] = UserORM
