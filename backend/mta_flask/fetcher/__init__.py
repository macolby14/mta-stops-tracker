import httpx
import asyncio

from ..proto import gtfs_realtime_pb2


class Fetcher:
    def __init__(self, url: str, api_key: str) -> None:
        self.url = url
        self.req_headers = {"x-api-key": api_key}

    async def fetch(self) -> bytes:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url, headers=self.req_headers)
            response.raise_for_status()
            return response.content

    async def fetch_and_parse(self) -> gtfs_realtime_pb2.FeedMessage:
        res = await self.fetch()
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(res)
        return feed


class FetchersGroup:
    def __init__(self, lines: list[str], api_key: str) -> None:
        self.line_to_fetchers = {
            "C": ACEFetcher(api_key),
            "A": ACEFetcher(api_key),
            "E": ACEFetcher(api_key),
            "B": BDFMFetcher(api_key),
            "D": BDFMFetcher(api_key),
            "F": BDFMFetcher(api_key),
            "M": BDFMFetcher(api_key),
            "G": GFetcher(api_key),
            "N": NQRWFetcher(api_key),
            "Q": NQRWFetcher(api_key),
            "R": NQRWFetcher(api_key),
            "W": NQRWFetcher(api_key),
            "J": JZFetcher(api_key),
            "Z": JZFetcher(api_key),
            "L": LFetcher(api_key),
            "1": NumberLineFetcher(api_key),
            "2": NumberLineFetcher(api_key),
            "3": NumberLineFetcher(api_key),
            "4": NumberLineFetcher(api_key),
            "5": NumberLineFetcher(api_key),
            "6": NumberLineFetcher(api_key),
            "7": NumberLineFetcher(api_key),
        }
        self.fetchers = set()
        for line in lines:
            self.fetchers.add(self.line_to_fetchers[line])

    async def fetch_and_parse(self) -> list[gtfs_realtime_pb2.FeedMessage]:
        return await asyncio.gather(
            *[fetcher.fetch_and_parse() for fetcher in self.fetchers]
        )


class ACEFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
            api_key,
        )


class BDFMFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
            api_key,
        )


class GFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g",
            api_key,
        )


class NQRWFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
            api_key,
        )


class JZFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz",
            api_key,
        )


class LFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l",
            api_key,
        )


class NumberLineFetcher(Fetcher):
    def __init__(self, api_key: str) -> None:
        super().__init__(
            "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
            api_key,
        )
