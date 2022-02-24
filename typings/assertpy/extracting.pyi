from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class ExtractingMixin:
    def extracting(self, *names: Any, **kwargs: Any) -> AssertionBuilder:
        ...
