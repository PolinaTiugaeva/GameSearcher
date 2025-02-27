"""Containers module."""

from dependency_injector import containers, providers
from .services import VectorDBService, QueueService
from loguru import logger



class Container(containers.DeclarativeContainer):

    config = providers.Configuration("config")
    # chromadb
    config.vec_host.from_env("VEC_HOST", required=True)
    config.vec_port.from_env("VEC_PORT", required=True)
    # queue service
    config.q_host.from_env("Q_HOST", required=True)
    config.q_port.from_env("Q_PORT", required=True)
    config.q_user.from_env("Q_USER", required=True)
    config.q_pass.from_env("Q_PASS", required=True)

    # Services

    vector_service = providers.Singleton(
        VectorDBService,
        host=config.vec_host,
        port=config.vec_port,
    )

    q_service = providers.Singleton(
        QueueService,
        config.q_host,
        config.q_port,
        config.q_user,
        config.q_pass,
    )
