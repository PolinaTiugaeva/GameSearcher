"""Services module."""
import chromadb
import pika
from loguru import logger

class VectorDBService():

    def __init__(self, host: str, port: int):
        self.client = chromadb.HttpClient(host=host, port=port)

    def get_collection(self, name: str) -> chromadb.Collection:
        return self.client.get_collection(name)

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
