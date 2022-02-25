import json
from typing import Any, Dict, Optional

import aiohttp

from .route import Route


class Client:
    # TODO : Add cache
    # cacheTime: ClassVar[Optional[float]] = None

    def __init__(
        self, connector: Optional[aiohttp.BaseConnector] = None
    ) -> None:
        self.connector = connector
        self.__session: aiohttp.ClientSession = aiohttp.ClientSession(
            connector=self.connector
        )

    async def request(
        self,
        route: Route,
        **kwargs: Any,
    ) -> Any:
        method = route.method
        url = route.url

        headers: Dict[str, str] = {}

        if 'json' in kwargs:
            headers['Content-Type'] = 'application/json'
            kwargs['data'] = json.dumps(
                kwargs.pop('json'), separators=(',', ':'), ensure_ascii=True
            )

        kwargs['headers'] = headers

        # TODO : Before each request, check if have cache
        async with self.__session.request(method, url, **kwargs) as response:
            return response

    def recreate(self) -> None:
        if self.__session.closed:
            self.__session = aiohttp.ClientSession(connector=self.connector)

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()
