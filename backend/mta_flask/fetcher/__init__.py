import httpx


class Fetcher(object):
    def __init__(self, url: str, api_key: str) -> None:
        self.url = url
        self.req_headers = {"x-api-key": api_key}

    async def fetch(self) -> bytes:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url, headers=self.req_headers)
            response.raise_for_status()
            return response.content


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
