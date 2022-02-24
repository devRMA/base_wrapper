from typing import Any, ClassVar
from urllib.parse import quote as _uriquote


class Route:
    BASE: ClassVar[str] = NotImplemented
    path: str
    method: str
    url: str

    def __init__(self, method: str, path: str, **parameters: Any) -> None:
        self.path = path
        self.method = method
        url = self.BASE + self.path
        if parameters:
            url = url.format_map(
                {
                    k: _uriquote(v) if isinstance(v, str) else v
                    for k, v in parameters.items()
                }
            )
        self.url = url
