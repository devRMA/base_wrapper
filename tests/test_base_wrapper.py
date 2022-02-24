from assertpy import assert_that

from base_wrapper import __version__
from scripts.bump_version import get_current_version


def describe_version() -> None:
    def version_equals_to_pyproject() -> None:
        assert_that(__version__).is_equal_to(str(get_current_version()))
