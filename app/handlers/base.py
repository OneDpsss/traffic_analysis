from abc import ABC, abstractmethod
from typing import Optional

from app.context import PipelineContext


class Handler(ABC):
    _next: Optional["Handler"] = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, context: PipelineContext) -> None:
        self.process(context)
        if self._next:
            self._next.handle(context)

    @abstractmethod
    def process(self, context: PipelineContext) -> None:
        ...
