"""Services module."""
import pika
from loguru import logger
from sqlmodel import create_engine, Session
from sqlalchemy import Engine

class QueueService():

    def __init__(self, host: str, port: int, username: str, password: str):
        self.connection_params = pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host="/",
            credentials=pika.PlainCredentials(
                username=username,
                password=password
            ),
            heartbeat=30,
            blocked_connection_timeout=20,
        )
        self.connection = pika.BlockingConnection(self.connection_params)
        self.chanel = self.connection.channel()

    def get_chanel(self) -> pika.channel:
        return self.chanel

class SQLDBService():

    def __init__(self, host: str, port: int, user: str, password: str, name: str):
        url = f'postgresql+psycopg://{user}:{password}@{host}:{port}/{name}'
        self.engine = create_engine(
            url=url,
            echo=True,
            pool_size=5,
            max_overflow=10,
        )
        self.session = Session(self.engine)

    def get_session(self) -> Session:
        return self.session

    def get_engine(self) -> Engine:
        return self.engine