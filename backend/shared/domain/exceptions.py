class EntityIdentifierAlreadySetError(ValueError):
    pass


class EntityIdentifierValueError(ValueError):
    pass


class RepositoryError(Exception):
    pass


class NoEntriesFoundError(RepositoryError):
    pass


class UnexpectedNumberOfEntriesFoundError(RepositoryError):
    pass
