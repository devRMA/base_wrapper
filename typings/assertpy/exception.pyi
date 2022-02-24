from typing import Any

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class ExceptionMixin:
    def raises(self, ex: Exception) -> AssertionBuilder:
        ...

    def when_called_with(
        self, *some_args: Any, **some_kwargs: Any
    ) -> AssertionBuilder:
        ...
