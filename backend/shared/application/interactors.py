from abc import ABC, abstractmethod


class InteractorResponse:
    def __init__(self, context: dict = None, success: bool = True):
        self._context = context or {}
        self._success = success

    @property
    def context(self) -> dict:
        return self._context

    @property
    def success(self) -> bool:
        return self._success


class ApplicationUseCase(ABC):
    @abstractmethod
    def execute(self) -> InteractorResponse: pass
