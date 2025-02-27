from chromadb import Collection
from dependency_injector.wiring import Provide, inject
from .containers import Container
from .services import VectorDBService, QueueService


@inject
def get_collection(vector: VectorDBService = Provide[Container.vector_service]) -> Collection:
    return vector.get_collection(name="games")

@inject
def get_chanel(q_service: QueueService = Provide[Container.q_service]):
    return q_service.get_chanel()

