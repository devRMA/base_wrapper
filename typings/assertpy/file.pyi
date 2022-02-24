from .assertpy import AssertionBuilder

__tracebackhide__: bool = ...


def contents_of(file: str, encoding: str = ...) -> str:
    ...


class FileMixin:
    def exists(self) -> AssertionBuilder:
        ...

    def does_not_exist(self) -> AssertionBuilder:
        ...

    def is_file(self) -> AssertionBuilder:
        ...

    def is_directory(self) -> AssertionBuilder:
        ...

    def is_named(self, filename: str) -> AssertionBuilder:
        ...

    def is_child_of(self, parent: str) -> AssertionBuilder:
        ...
