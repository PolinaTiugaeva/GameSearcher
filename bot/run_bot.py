import asyncio
import datetime
import os

from dotenv import load_dotenv
from loguru import logger

from base import Bot


def run():
    
    loop = asyncio.get_event_loop()

    local_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(local_dotenv_path):
        load_dotenv(local_dotenv_path)
    bot_token = os.environ['BOT_TOKEN']
    bot = Bot(bot_token, 1)
    try:
        loop.create_task(bot.start())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(bot.stop())
        

if __name__ == '__main__':
    run()
