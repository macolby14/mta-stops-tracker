import httpx

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


class FetcherFactory:
    def create(self, line: str, api_key: str) -> Fetcher:
        if line == "A" or line == "C" or line == "E":
            return ACEFetcher(api_key)
        elif line == "B" or line == "D" or line == "F" or line == "M":
            return BDFMFetcher(api_key)
        elif line == "G":
            return GFetcher(api_key)
        elif line == "N" or line == "Q" or line == "R" or line == "W":
            return NQRWFetcher(api_key)
        elif line == "J" or line == "Z":
            return JZFetcher(api_key)
        elif line == "L":
            return LFetcher(api_key)
        elif (
            line == "1"
            or line == "2"
            or line == "3"
            or line == "4"
            or line == "5"
            or line == "6"
            or line == "7"
        ):
            return NumberLineFetcher(api_key)
        else:
            raise ValueError(f"Invalid line: {line}")


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
