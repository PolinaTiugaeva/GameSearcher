from dependency_injector.wiring import Provide, inject
from sqlmodel import Session
from .containers import Container
from .services import QueueService, SQLDBService

@inject
def get_chanel(q_service: QueueService = Provide[Container.q_service]):
    return q_service.get_chanel()

@inject
def get_session(sql: SQLDBService = Provide[Container.sql_service]) -> Session:
    return sql.get_session()
