from abc import ABC
from typing import Type, List

from django.db.models import Manager

from backend.shared.domain import exceptions
from backend.shared.domain.entities import DomainEntity
from backend.shared.domain.repositories import EntityRepository, EntityFilter
from backend.shared.infrastructure.mappers import EntityMapper


class FilterDatabaseApplier:
    @classmethod
    def apply_filter(cls, resource: Manager, entity_filter: EntityFilter):

        filters = {
            cls._format_filter_key(entity_filter): entity_filter.value
        }

        if 'not' in entity_filter.filter_type:
            return resource.exclude(**filters)

        return resource.filter(**filters)

    @staticmethod
    def _format_filter_key(entity_filter: EntityFilter):
        filter_type = entity_filter.filter_type.replace('not', '').strip()
        filter_mapper = {
            'is': '',
            'contains': '__contains',
            'in': '__in',
        }

        return f'{entity_filter.key}{filter_mapper[filter_type]}'


class DatabaseEntityRepository(EntityRepository, ABC):
    entity_mapper: Type[EntityMapper]
    filter_applier = FilterDatabaseApplier

    def find_one_by_id(self, entity_id) -> DomainEntity:
        try:
            model = self.entity_mapper.objects.get(id=entity_id)
        except self.entity_mapper.DoesNotExist:
            raise exceptions.NoEntriesFoundError
        except self.entity_mapper.MultipleObjectsReturned:
            raise exceptions.UnexpectedNumberOfEntriesFoundError

        return model.entity

    def find_by(self, **filter_params) -> List[DomainEntity]:
        results = self.entity_mapper.objects.filter(**filter_params).order_by('id')
        if not results:
            return []

        entities = [result.entity for result in results]

        return entities

    def find_all(self):
        results = self.entity_mapper.objects.all()
        entities = []
        for result in results:
            entities.append(result.entity)

        return entities

    def save(self, entity: DomainEntity):
        mapper = self.entity_mapper.create_from_entity(entity)
        mapper.save()
        entity.__dict__ = mapper.entity.__dict__

    def _execute_filtered_query(self, filters):
        query = self.entity_mapper.objects
        for entity_filter in filters:
            query = self.filter_applier.apply_filter(
                query,
                entity_filter
            )
        return query
