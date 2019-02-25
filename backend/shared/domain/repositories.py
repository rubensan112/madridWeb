from abc import ABC


class EntityRepository(ABC):
    @staticmethod
    def calculate_initial_offset(items_per_page: int, page: int) -> int:
        a = 1 - items_per_page
        b = page * items_per_page
        return a + b


class EntityFilter:
    VALID_FILTER_TYPE = [
        'is',
        'is not',
        'contains',
        'not contains',
        'in',
        'not in',
    ]

    def __init__(self, key: str, filter_type: str, value):
        self.key = key
        self.filter_type = filter_type
        self.value = value

    @property
    def filter_type(self) -> str:
        return self._filter_type

    @filter_type.setter
    def filter_type(self, value):
        if value not in self.VALID_FILTER_TYPE:
            # TODO: raise custom exception
            raise ValueError
        self._filter_type = value


class PaginationInformation:
    def __init__(self, page: int, items_per_page: int):
        self.page = page
        self.items_per_page = items_per_page


class SortingInformation:
    def __init__(self, sort_by: str, sort_order: str = 'asc'):
        self.sort_by = sort_by
        self.sort_order = sort_order
