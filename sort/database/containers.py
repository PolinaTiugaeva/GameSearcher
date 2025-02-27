"""Containers module."""

from dependency_injector import containers, providers
from .services import QueueService, SQLDBService
from loguru import logger



class Container(containers.DeclarativeContainer):

    config = providers.Configuration("config")
    # queue service
    config.q_host.from_env("Q_HOST", required=True)
    config.q_port.from_env("Q_PORT", required=True)
    config.q_user.from_env("Q_USER", required=True)
    config.q_pass.from_env("Q_PASS", required=True)
    # sql
    config.sql_host.from_env("SQL_HOST", required=True)
    config.sql_port.from_env("SQL_PORT", required=True)
    config.sql_user.from_env("SQL_USER", required=True)
    config.sql_pass.from_env("SQL_PASS", required=True)
    config.sql_name.from_env("SQL_NAME", required=True)

    # Services

    sql_service = providers.Singleton(
        SQLDBService,
        config.sql_host,
        config.sql_port,
        config.sql_user,
        config.sql_pass,
        config.sql_name,
    )

    q_service = providers.Singleton(
        QueueService,
        config.q_host,
        config.q_port,
        config.q_user,
        config.q_pass,
    )
