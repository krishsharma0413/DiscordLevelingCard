from aiohttp import ClientSession

class DiscordLevelingCard:
    pass

class RequestHandler:
    __session: ClientSession = ClientSession()

    def __init__(self, session: ClientSession = __session):
        self.session = session
    
    async def get(self, url: str) -> bytes:
        async with self.session.get(url) as response:
            return await response.read()
    
    async def close(self):
        await self.session.close()    