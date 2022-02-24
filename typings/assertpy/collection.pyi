from typing import Any, Callable

from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


class CollectionMixin:
    def is_iterable(self) -> AssertionBuilder:
        ...

    def is_not_iterable(self) -> AssertionBuilder:
        ...

    def is_subset_of(self, *supersets: Any) -> AssertionBuilder:
        ...

    def is_sorted(
        self,
        key: Callable[[Any], Any] = ...,
        reverse: bool = ...
    ) -> AssertionBuilder:
        ...
