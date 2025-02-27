import json
import os
import pandas as pd
import pika
from loguru import logger
from database.containers import Container
from database.database import get_collection, get_chanel


df_games = pd.read_csv('games.csv')

def process_request(ch, method, properties, body):
    message = json.loads(body)
    collection = get_collection()
    result = collection.query(
        query_texts=[message['text']]
    )
    #logger.info(result)
    search_result = []
    for game_score in zip(result['ids'][0], result['distances'][0]):
        game_title = df_games[df_games['app_id'] == int(game_score[0])]['title'].astype(str).values[0]
        search_result.append((game_title, game_score[1]))
    responce = json.dumps({
        "username" : message['username'],
        "chat_id" : message['chat_id'],
        "titles" : search_result
    })
    ch.basic_publish(
        exchange='',
        routing_key='sort_request',
        body=responce,
        properties=pika.BasicProperties(
            delivery_mode=2
        )        
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)



if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__], packages=["database"])
    collection = get_collection()
    collection.query(query_texts=["aaa"])
    chanel = get_chanel()
    chanel.queue_declare(queue='search_request', durable=True)
    chanel.basic_consume(queue='search_request', on_message_callback=process_request)
    logger.info("Start consumption")
    chanel.start_consuming()