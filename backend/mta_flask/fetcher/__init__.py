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
    def __init__(self, lines: set[str], api_key: str) -> None:
        self.line_to_line_group = {
            "C": "ACE",
            "A": "ACE",
            "E": "ACE",
            "B": "BDFM",
            "D": "BDFM",
            "F": "BDFM",
            "M": "BDFM",
            "G": "G",
            "N": "NQRW",
            "Q": "NQRW",
            "R": "NQRW",
            "W": "NQRW",
            "J": "JZ",
            "Z": "JZ",
            "L": "L",
            "1": "1234567",
            "2": "1234567",
            "3": "1234567",
            "4": "1234567",
            "5": "1234567",
            "6": "1234567",
            "7": "1234567",
        }

        self.line_group_to_fetchers = {
            "ACE": ACEFetcher(api_key),
            "BDFM": BDFMFetcher(api_key),
            "G": GFetcher(api_key),
            "NQRW": NQRWFetcher(api_key),
            "JZ": JZFetcher(api_key),
            "L": LFetcher(api_key),
            "1234567": NumberLineFetcher(api_key),
        }
        self.fetchers = set()
        line_groups = set()
        for line in lines:
            line_groups.add(self.line_to_line_group[line])
        for line_group in line_groups:
            self.fetchers.add(self.line_group_to_fetchers[line_group])

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
