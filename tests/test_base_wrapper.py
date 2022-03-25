from assertpy import assert_that

from base_wrapper import __version__
from base_wrapper.route import Route
from scripts.bump_version import get_current_version


def describe_version() -> None:
    def version_equals_to_pyproject() -> None:
        assert_that(__version__).is_equal_to(str(get_current_version()))


def describe_route() -> None:
    Route.BASE = 'https://example.com'

    def path_equals_to_url() -> None:
        assert_that(Route('GET', '/').path).is_equal_to('/')

    def url_equals_to_base_url_with_path() -> None:
        assert_that(Route('GET', '/').url).is_equal_to('https://example.com/')

    def method_equals_to_given_method() -> None:
        assert_that(Route('GET', '/').method).is_equal_to('GET')

    def params_equals_to_given_params() -> None:
        url = Route('GET', '/{foo}', foo='bar').url
        assert_that(url).is_equal_to('https://example.com/bar')


# TODO : Add tests for Client
