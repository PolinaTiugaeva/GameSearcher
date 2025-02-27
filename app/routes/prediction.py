from fastapi import APIRouter, Depends, Request, HTTPException
import json
import pika

from database.config import get_settings
from depends.rabbitmq.chanel import get_channel, get_queue_request_name, get_queue_responce_name
from loguru import logger
from typing import Annotated

prediction_route = APIRouter(tags=['prediction'])

@prediction_route.post('/')
async def request(request: Request, channel: Annotated[pika.adapters.blocking_connection.BlockingChannel, Depends(get_channel)]):
    body = await request.body()
    channel.basic_publish(
        exchange='',
        routing_key=get_queue_request_name(),
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )
    channel.basic_ack()
    return 200

@prediction_route.get('/')
async def responce(channel: Annotated[pika.adapters.blocking_connection.BlockingChannel, Depends(get_channel)]):
    method_frame, header_frame, body = channel.basic_get(get_queue_responce_name())
    
    if method_frame is not None:
        # Преобразование тела сообщения в строку
        message = body.decode("utf-8")
        # Подтверждение получения сообщения
        channel.basic_ack(method_frame.delivery_tag)
        message = json.loads(message)
        return message
    else:
        return None