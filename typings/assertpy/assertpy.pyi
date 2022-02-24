from __future__ import annotations

import contextlib
import logging
from typing import Any, Callable, Dict, Generator, List, MutableMapping

from .base import BaseMixin
from .collection import CollectionMixin
from .contains import ContainsMixin
from .date import DateMixin
from .dict import DictMixin
from .dynamic import DynamicMixin
from .exception import ExceptionMixin
from .extracting import ExtractingMixin
from .file import FileMixin
from .helpers import HelpersMixin
from .numeric import NumericMixin
from .snapshot import SnapshotMixin
from .string import StringMixin

__version__: str = ...
__tracebackhide__: bool = ...
ASSERTPY_FILES: List[str] = ...
_soft_ctx: int = ...
_soft_err: List[str] = ...


@contextlib.contextmanager
def soft_assertions() -> Generator[None, None, None]:
    ...


def assert_that(val: Any, description: str = ...) -> AssertionBuilder:
    ...


def assert_warn(
    val: Any,
    description: str = ...,
    logger: logging.Logger = ...
) -> AssertionBuilder:
    ...


def fail(msg: str = ...) -> AssertionError:
    ...


def soft_fail(msg: str = ...) -> None:
    ...


_extensions: Dict[str, Callable[..., Any]] = ...


def add_extension(func: Callable[..., Any]) -> None:
    ...


def remove_extension(func: Callable[..., Any]) -> None:
    ...


class WarningLoggingAdapter(logging.LoggerAdapter):  # type: ignore
    def process(self, msg: str,
                kwargs: Any) -> tuple[str, MutableMapping[str, Any]]:
        ...


_logger: logging.Logger = ...
_handler: logging.StreamHandler = ...  # type: ignore
_format: logging.Formatter = ...
_default_logger: WarningLoggingAdapter = ...


class AssertionBuilder(
    StringMixin, SnapshotMixin, NumericMixin, HelpersMixin, FileMixin,
    ExtractingMixin, ExceptionMixin, DynamicMixin, DictMixin, DateMixin,
    ContainsMixin, CollectionMixin, BaseMixin
):
    def __init__(
        self,
        val: Any,
        description: str | None = ...,
        kind: str | None = ...,
        expected: Exception | None = ...,
        logger: logging.Logger | None = ...
    ) -> None:
        ...

    def builder(
        self,
        val: Any,
        description: str | None = ...,
        kind: str | None = ...,
        expected: Exception | None = ...,
        logger: logging.Logger | None = ...
    ) -> AssertionBuilder:
        ...

    def error(self, msg: str) -> AssertionBuilder:
        ...
