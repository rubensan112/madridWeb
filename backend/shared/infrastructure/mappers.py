from abc import abstractmethod

from django.db import models


class EntityMapper(models.Model):
    @classmethod
    @abstractmethod
    def create_from_entity(cls, entity): pass

    @property
    @abstractmethod
    def entity(self): pass

    class Meta:
        abstract = True
