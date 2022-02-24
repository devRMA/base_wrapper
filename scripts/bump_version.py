from typing import Any, Dict, MutableMapping

from semantic_version import Version
from toml import load


def get_current_version() -> Version:
    with open('pyproject.toml', 'r', encoding='utf-8') as file:
        data: MutableMapping[str, Any] = load(file)
    tool: Dict[str, Any] = data.get('tool', {})
    poetry: Dict[str, Any] = tool.get('poetry', {})
    return Version.coerce(poetry.get('version', '0.1.0'))


def bump_major() -> None:
    version = get_current_version().next_major()
    _change_version(version)
    print(f'Major version bumped to: {version}')


def bump_minor() -> None:
    version = get_current_version().next_minor()
    _change_version(version)
    print(f'Minor version bumped to: {version}')


def bump_patch() -> None:
    version = get_current_version().next_patch()
    _change_version(version)
    print(f'Patch version bumped to: {version}')


def _change_pyproject_version(version: Version) -> None:
    with open('pyproject.toml', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('version ='):
            lines[i] = f'version = "{version}"\n'

    with open('pyproject.toml', 'w', encoding='utf-8') as file:
        file.writelines(lines)


def _change_module_version(version: Version) -> None:
    with open('base_wrapper/__init__.py', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith('__version__ = '):
            lines[i] = f"__version__ = '{version}'\n"

    with open('base_wrapper/__init__.py', 'w', encoding='utf-8') as file:
        file.writelines(lines)


def _change_version(version: Version) -> None:
    _change_pyproject_version(version)
    _change_module_version(version)
