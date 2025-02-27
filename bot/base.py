import asyncio

from loguru import logger
from poller import Poller
from notifier import Notifier


class Bot:
    def __init__(self, token: str, n: int = 1):
        self.poller = Poller(token)
        self.notifier = Notifier(token, n)

    async def start(self):
        await self.poller.start()
        await self.notifier.start()

    async def stop(self):
        await self.poller.stop()
        await self.notifier.stop()
