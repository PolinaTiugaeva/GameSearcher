import asyncio
import aiohttp
from asyncio import Task
from loguru import logger
from typing import Optional

from clients.tg.api import TgClient


class Poller:
    def __init__(self, token: str):
        self.tg_client = TgClient(token)
        self._task: Optional[Task] = None

    async def _worker(self):
        offset = 0
        while True:
            res = await self.tg_client.get_updates_in_objects(offset=offset, timeout=60)
            logger.info(res)
            for u in res.result:
                offset = u.update_id + 1
                if u.message:
                    json = {
                        'username' : u.message.from_.username,
                        'chat_id' : u.message.chat.id,
                        'text' : u.message.text
                    }
                    async with aiohttp.ClientSession() as session:
                        responce = await session.post(
                            'http://app:8080/prediction/',
                            json=json,
                            timeout=1
                        )
                if u.callback_query:
                    json = {
                        'username' : u.callback_query.message.from_.username,
                        'game_title' : u.callback_query.message.text,
                        'reaction' : u.callback_query.data
                    }
                    logger.info(json)
                    async with aiohttp.ClientSession() as session:
                        responce = await session.post(
                            'http://app:8080/history/reaction/',
                            json=json,
                            timeout=1
                        )
                        logger.info(await responce.json())
                    

    async def start(self):
        self._task = asyncio.create_task(self._worker())

    async def stop(self):
        self._task.cancel()
