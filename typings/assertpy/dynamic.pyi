from typing import Any

__tracebackhide__: bool = ...


class DynamicMixin:
    def __getattr__(self, attr: str) -> Any:
        ...
