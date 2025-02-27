import asyncio
import aiohttp
import datetime
from loguru import logger
from typing import List

from clients.tg.api import TgClient
from clients.tg.dcs import UpdateObj


class Notifier:
    def __init__(self, token: str, concurrent_workers: int):
        self.tg_client = TgClient(token)
        self.concurrent_workers = concurrent_workers
        self._tasks: List[asyncio.Task] = []

    async def handle_update(self, upd):
        button1 = {
            'text' : '\U0001F44D',
            'callback_data': "1"
        }
        button2 = {
            'text' : '\U0001F44E',
            'callback_data': "0"
        }
        markup = [
            [
                button1, button2
            ]
        ]
        for u in upd['game_scores']:
            await self.tg_client.send_message_with_reply_markup(upd["chat_id"], u[0], markup)

    async def _worker(self):
        while True:
            async with aiohttp.ClientSession() as session:
                responce = await session.get(
                    'http://app:8080/prediction/',
                    timeout=1
                )
                json = await responce.json()
            if json:
                await self.handle_update(json)

    async def start(self):
        self._tasks = [asyncio.create_task(self._worker()) for _ in range(self.concurrent_workers)]

    async def stop(self):
        await self.queue.join()
        for t in self._tasks:
            t.cancel()
