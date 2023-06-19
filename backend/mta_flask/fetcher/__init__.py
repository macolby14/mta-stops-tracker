from aiohttp import ClientSession


class Fetcher(object):
    def __init__(self, url: str, session: ClientSession) -> None:
        self.url = url
        self.session = session

    async def fetch(self) -> str:
        response = await self.session.get(self.url)
        response.raise_for_status()
        return await response.text()


class ACEFetcher(Fetcher):
    session: ClientSession

    def __init__(self) -> None:
        # Create a session if one doesn't exist. Single lifetime session for Fetchers of this type # noqa
        if not self.__class__.session:
            self.__class__.session = ClientSession()

        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
            self.__class__.session,
        )


class BDFMFetcher(Fetcher):
    session: ClientSession

    def __init__(self) -> None:
        # Create a session if one doesn't exist. Single lifetime session for Fetchers of this type # noqa
        if not self.__class__.session:
            self.__class__.session = ClientSession()

        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
            self.__class__.session,
        )
